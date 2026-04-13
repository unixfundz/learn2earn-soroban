import strawberry
from datetime import datetime
from typing import Optional, List
from .models import ContractEvent


@strawberry.type
class ContractEventType:
    id: int
    event_type: str
    tx_hash: str
    ledger: int
    topic: str
    payload: str
    emitted_at: datetime
    contract_id: str


@strawberry.type
class Query:
    @strawberry.field
    def events(
        self,
        contract_id: Optional[str] = None,
        event_type: Optional[str] = None,
        ledger_from: Optional[int] = None,
        ledger_to: Optional[int] = None,
    ) -> List[ContractEventType]:
        queryset = ContractEvent.objects.select_related("tracked_contract").all()
        if contract_id:
            queryset = queryset.filter(tracked_contract__contract_id=contract_id)
        if event_type:
            queryset = queryset.filter(event_type=event_type)
        if ledger_from is not None:
            queryset = queryset.filter(ledger__gte=ledger_from)
        if ledger_to is not None:
            queryset = queryset.filter(ledger__lte=ledger_to)

        return [
            ContractEventType(
                id=e.id,
                event_type=e.event_type,
                tx_hash=e.tx_hash,
                ledger=e.ledger,
                topic=e.topic,
                payload=str(e.payload),
                emitted_at=e.emitted_at,
                contract_id=e.tracked_contract.contract_id,
            )
            for e in queryset[:200]
        ]


schema = strawberry.Schema(query=Query)
