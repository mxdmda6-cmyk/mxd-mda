from __future__ import annotations

import datetime as dt
from typing import Any


class SocialNeuron:
    """Dry-run social neuron.

    This object intentionally never publishes. It only reports what would have
    been prepared if a future reviewed task enables a real integration.
    """

    def prepare(
        self,
        text: str,
        platforms: list[str],
        when: str | None = None,
    ) -> dict[str, Any]:
        """Return a dry-run publication preview without external side effects."""
        return {
            "published": False,
            "mode": "dry_run",
            "would_publish": True,
            "platforms": platforms,
            "scheduled_for": when,
            "prepared_at_utc": dt.datetime.now(dt.UTC).isoformat(),
            "external_ids": {},
            "preview_text": text,
        }


social_neuron = SocialNeuron()
