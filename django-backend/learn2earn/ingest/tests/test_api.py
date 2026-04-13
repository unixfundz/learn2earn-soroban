import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from ingest.models import TrackedContract, ContractEvent
from django.utils import timezone


@pytest.mark.django_db
def test_event_list_endpoint():
    client = APIClient()
    contract = TrackedContract.objects.create(contract_id="CABC", label="Demo")
    ContractEvent.objects.create(
        tracked_contract=contract,
        event_type="transfer",
        tx_hash="tx-1",
        ledger=123,
        event_index=0,
        topic="asset",
        payload={"amount": "100"},
        emitted_at=timezone.now(),
    )

    resp = client.get("/api/events/")
    assert resp.status_code == 200
    assert len(resp.json()) == 1
