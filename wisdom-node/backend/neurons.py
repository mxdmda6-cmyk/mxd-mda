from __future__ import annotations
from typing import Any, Dict, List
import datetime as dt

class SocialNeuron:
    """
    Stub neuron. Swap this with Buffer/Meta/TikTok integrations later.
    """
    def publish(self, text: str, platforms: List[str], when: str | None = None) -> Dict[str, Any]:
        # when: ISO timestamp or None = publish now
        return {
            "published": True,
            "platforms": platforms,
            "scheduled_for": when,
            "external_ids": {p: f"stub_{p}_{int(dt.datetime.utcnow().timestamp())}" for p in platforms}
        }

social_neuron = SocialNeuron()
