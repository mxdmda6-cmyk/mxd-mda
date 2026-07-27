"""Environment-backed settings with publishing paths sealed by default."""

from __future__ import annotations

import os
from dataclasses import dataclass


def _env_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    database_url: str = "postgresql+psycopg://mxd_mda:mxd_mda@localhost:5432/mxd_mda"
    webhook_shared_secret: str | None = None
    enable_notion_sync: bool = False
    enable_shopify_integration: bool = False
    enable_github_webhooks: bool = False
    enable_asset_validation_jobs: bool = True
    enable_agent_jobs: bool = False
    enable_backup_exports: bool = False
    enable_live_publishing: bool = False
    enable_shopify_writes: bool = False

    def __post_init__(self) -> None:
        if self.enable_live_publishing or self.enable_shopify_writes:
            raise ValueError(
                "Publishing and Shopify writes must remain disabled in the MVP"
            )

    @classmethod
    def from_env(cls) -> Settings:
        return cls(
            database_url=os.getenv("DATABASE_URL", cls.database_url),
            webhook_shared_secret=os.getenv("WEBHOOK_SHARED_SECRET") or None,
            enable_notion_sync=_env_bool("ENABLE_NOTION_SYNC"),
            enable_shopify_integration=_env_bool("ENABLE_SHOPIFY_INTEGRATION"),
            enable_github_webhooks=_env_bool("ENABLE_GITHUB_WEBHOOKS"),
            enable_asset_validation_jobs=_env_bool(
                "ENABLE_ASSET_VALIDATION_JOBS", True
            ),
            enable_agent_jobs=_env_bool("ENABLE_AGENT_JOBS"),
            enable_backup_exports=_env_bool("ENABLE_BACKUP_EXPORTS"),
            enable_live_publishing=_env_bool("ENABLE_LIVE_PUBLISHING"),
            enable_shopify_writes=_env_bool("ENABLE_SHOPIFY_WRITES"),
        )
