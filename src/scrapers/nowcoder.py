"""Nowcoder campus recruiting job scraper."""

import asyncio
import json
import logging
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterator, List, Optional
from urllib.parse import quote_plus

import httpx

from .base import BaseScraper, FetchResult
from ..models import ContentItem, NowcoderConfig, SourceType

logger = logging.getLogger(__name__)

JOBS_URL = "https://www.nowcoder.com/jobs/school/jobs"
JOB_DETAIL_URL = "https://www.nowcoder.com/jobs/detail/{job_id}"
STATE_MARKER = "window.__INITIAL_STATE__="
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
EDU_LABELS = {
    0: "学历不限",
    5000: "本科",
    6000: "硕士",
    7000: "博士",
}
EXCLUDED_EDU_LEVELS = {6000, 7000}


class NowcoderScraper(BaseScraper):
    """Fetch campus recruiting jobs from Nowcoder search pages."""

    def __init__(self, config: NowcoderConfig, http_client: httpx.AsyncClient):
        super().__init__(config.model_dump(), http_client)
        self.nowcoder_config = config

    async def fetch(self, since: datetime) -> FetchResult:
        result = FetchResult()
        if not self.config.get("enabled", True):
            return result

        tasks = [
            result.collect(query, self._fetch_query(query))
            for query in self.nowcoder_config.queries
        ]
        await asyncio.gather(*tasks)

        cutoff = datetime.now(timezone.utc) - timedelta(
            days=self.nowcoder_config.max_age_days
        )
        seen = self._load_seen()
        seen_set = set(seen)
        unique: dict[str, ContentItem] = {}
        for item in result.items:
            if item.published_at < cutoff or item.id in seen_set:
                continue
            existing = unique.get(item.id)
            if existing is None:
                unique[item.id] = item
            elif existing.author == "未知公司" and item.author != "未知公司":
                unique[item.id] = item
            elif item.published_at > existing.published_at:
                unique[item.id] = item

        result.items = sorted(
            unique.values(), key=lambda item: item.published_at, reverse=True
        )[: self.nowcoder_config.max_items]
        self._save_seen(seen, result.items)
        return result

    def _load_seen(self) -> List[str]:
        path = Path(self.nowcoder_config.state_file)
        if not path.is_absolute():
            path = Path.cwd() / path
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return []
        if isinstance(payload, dict):
            payload = payload.get("ids", [])
        if not isinstance(payload, list):
            return []
        return [str(value) for value in payload]

    def _save_seen(self, seen: List[str], items: List[ContentItem]) -> None:
        new_ids = [item.id for item in items if item.id not in set(seen)]
        if not new_ids:
            return
        merged = list(dict.fromkeys([*seen, *new_ids]))[-3000:]
        path = Path(self.nowcoder_config.state_file)
        if not path.is_absolute():
            path = Path.cwd() / path
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            temp_path = path.with_suffix(path.suffix + ".tmp")
            temp_path.write_text(
                json.dumps({"ids": merged}, ensure_ascii=False),
                encoding="utf-8",
            )
            temp_path.replace(path)
        except OSError as exc:
            logger.warning("Could not persist Nowcoder seen state: %s", exc)

    async def _fetch_query(self, query: str) -> List[ContentItem]:
        url = f"{JOBS_URL}?search={quote_plus(query)}"
        response = await self.client.get(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Referer": JOBS_URL,
            },
            timeout=45.0,
            follow_redirects=True,
        )
        response.raise_for_status()
        state = self._parse_state(response.text)
        if state is None:
            logger.warning("Nowcoder page has no embedded state for query %s", query)
            return []

        items: List[ContentItem] = []
        for job in self._iter_jobs(state):
            item = self._build_item(job, query)
            if item is not None:
                items.append(item)
        logger.info("Nowcoder query %s returned %d usable jobs", query, len(items))
        return items

    @staticmethod
    def _parse_state(html: str) -> Optional[Any]:
        marker = html.find(STATE_MARKER)
        if marker < 0:
            return None
        start = marker + len(STATE_MARKER)
        try:
            state, _ = json.JSONDecoder().raw_decode(html[start:])
        except json.JSONDecodeError:
            return None
        return state

    @classmethod
    def _iter_jobs(cls, node: Any) -> Iterator[dict]:
        if isinstance(node, dict):
            if (
                "jobName" in node
                and "id" in node
                and ("recruitType" in node or "companyId" in node)
            ):
                yield node
            for value in node.values():
                yield from cls._iter_jobs(value)
        elif isinstance(node, list):
            for value in node:
                yield from cls._iter_jobs(value)

    def _build_item(self, job: dict, query: str) -> Optional[ContentItem]:
        if job.get("recruitType") != 1:
            return None

        edu_level = job.get("eduLevel")
        if isinstance(edu_level, int) and edu_level in EXCLUDED_EDU_LEVELS:
            return None

        job_id = job.get("id")
        job_name = (job.get("jobName") or "").strip()
        if not job_id or not job_name:
            return None

        company = (job.get("companyNameText") or job.get("companyName") or "").strip()
        company = company or "未知公司"

        published_at = self._job_time(job)
        if published_at is None:
            return None

        cities = job.get("jobCityList") or (
            [job["jobCity"]] if job.get("jobCity") else []
        )
        city = "、".join(str(value) for value in cities if value)
        graduation = (job.get("graduationYear") or "").strip()
        salary = (job.get("salaryText") or "").strip()
        edu_label = (
            EDU_LABELS.get(edu_level, "学历未标明")
            if isinstance(edu_level, int)
            else "学历未标明"
        )

        ext = self._parse_ext(job.get("ext"))
        requirements = (ext.get("requirements") or "").strip()
        duties = (ext.get("infos") or "").strip()

        parts = [
            f"公司：{company}",
            f"岗位：{job_name}",
            f"城市：{city or '未标明'}",
            f"学历要求：{edu_label}",
            f"届别：{graduation or '未标明'}",
            f"薪资：{salary or '未标明'}",
        ]
        if requirements:
            parts.append(f"\n岗位要求：\n{requirements}")
        if duties:
            parts.append(f"\n岗位职责：\n{duties}")

        metadata = {
            "source_name": "nowcoder",
            "company": company,
            "job_city": city,
            "edu_level": edu_label,
            "graduation_year": graduation,
            "query": query,
        }
        if self.nowcoder_config.category:
            metadata["category"] = self.nowcoder_config.category
        external_url = (job.get("redirectExternalUrl") or "").strip()
        if external_url:
            metadata["apply_url"] = external_url

        return ContentItem(
            id=self._generate_id("nowcoder", "job", str(job_id)),
            source_type=SourceType.NOWCODER,
            title=f"{company}｜{job_name}",
            url=JOB_DETAIL_URL.format(job_id=job_id),
            content="\n".join(parts),
            author=company,
            published_at=published_at,
            profile=self.nowcoder_config.profile,
            metadata=metadata,
        )

    @staticmethod
    def _job_time(job: dict) -> Optional[datetime]:
        for key in ("createTime", "updateTime"):
            value = job.get(key)
            if isinstance(value, (int, float)) and value > 0:
                return datetime.fromtimestamp(value / 1000, tz=timezone.utc)
        return None

    @staticmethod
    def _parse_ext(value: Any) -> dict:
        if not isinstance(value, str):
            return {}
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            return {}
        return parsed if isinstance(parsed, dict) else {}
