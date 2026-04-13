from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ContractEvent, WebhookSubscription
from .tasks import dispatch_webhook


@receiver(post_save, sender=ContractEvent)
def fanout_webhooks(sender, instance: ContractEvent, created: bool, **kwargs):
    if not created:
        return

    subscriptions = WebhookSubscription.objects.filter(is_active=True)
    for sub in subscriptions:
        if sub.event_type and sub.event_type != instance.event_type:
            continue
        if sub.tracked_contract and sub.tracked_contract_id != instance.tracked_contract_id:
            continue
        dispatch_webhook.delay(sub.id, instance.id)
