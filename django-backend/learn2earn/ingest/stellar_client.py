from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List
from django.conf import settings
from stellar_sdk import Server


@dataclass
class ParsedEvent:
    contract_id: str
    event_type: str
    tx_hash: str
    ledger: int
    event_index: int
    topic: str
    payload: dict
    emitted_at: datetime


class StellarEventClient:
    def __init__(self) -> None:
        self.server = Server(horizon_url=settings.HORIZON_URL)

    def fetch_events(self, contract_id: str, cursor: str = "now", limit: int = 50) -> List[ParsedEvent]:
        # Placeholder structure for a production extension point.
        # This can be replaced with Soroban RPC event streaming as APIs evolve.
        _ = self.server
        return [
            ParsedEvent(
                contract_id=contract_id,
                event_type="heartbeat",
                tx_hash=f"mock-{cursor}",
                ledger=0,
                event_index=0,
                topic="system",
                payload={"status": "ok"},
                emitted_at=datetime.now(timezone.utc),
            )
        ]
