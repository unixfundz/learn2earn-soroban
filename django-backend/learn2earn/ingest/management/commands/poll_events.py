from django.core.management.base import BaseCommand
from django.utils import timezone
from ingest.models import ContractEvent, TrackedContract
from ingest.stellar_client import StellarEventClient


class Command(BaseCommand):
    help = "Poll events for tracked contracts"

    def handle(self, *args, **options):
        client = StellarEventClient()
        for tracked in TrackedContract.objects.filter(is_active=True):
            events = client.fetch_events(contract_id=tracked.contract_id)
            for item in events:
                ContractEvent.objects.get_or_create(
                    tracked_contract=tracked,
                    tx_hash=item.tx_hash,
                    event_index=item.event_index,
                    defaults={
                        "event_type": item.event_type,
                        "ledger": item.ledger,
                        "topic": item.topic,
                        "payload": item.payload,
                        "emitted_at": item.emitted_at or timezone.now(),
                    },
                )
        self.stdout.write(self.style.SUCCESS("Event polling completed"))
