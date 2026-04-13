import hashlib
import hmac
import json
import requests
from celery import shared_task
from django.conf import settings
from .models import ContractEvent, WebhookSubscription


def _sign(secret: str, payload: bytes) -> str:
    return hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()


@shared_task(bind=True, autoretry_for=(requests.RequestException,), retry_backoff=True, max_retries=5)
def dispatch_webhook(self, subscription_id: int, event_id: int) -> int:
    subscription = WebhookSubscription.objects.get(id=subscription_id, is_active=True)
    event = ContractEvent.objects.select_related("tracked_contract").get(id=event_id)

    payload_dict = {
        "id": event.id,
        "contract_id": event.tracked_contract.contract_id,
        "event_type": event.event_type,
        "tx_hash": event.tx_hash,
        "ledger": event.ledger,
        "event_index": event.event_index,
        "topic": event.topic,
        "payload": event.payload,
        "emitted_at": event.emitted_at.isoformat(),
    }
    payload = json.dumps(payload_dict, separators=(",", ":")).encode()
    signature = _sign(subscription.secret, payload)

    response = requests.post(
        subscription.target_url,
        data=payload,
        timeout=settings.WEBHOOK_TIMEOUT_SECONDS,
        headers={
            "Content-Type": "application/json",
            "X-Learn2Earn Soroban-Signature": signature,
        },
    )
    response.raise_for_status()
    return response.status_code
