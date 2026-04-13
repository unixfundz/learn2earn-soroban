from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TrackedContract(TimeStampedModel):
    contract_id = models.CharField(max_length=128, unique=True)
    label = models.CharField(max_length=120, blank=True)
    is_active = models.BooleanField(default=True)
    start_ledger = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        return self.label or self.contract_id


class ContractEvent(TimeStampedModel):
    tracked_contract = models.ForeignKey(TrackedContract, on_delete=models.CASCADE, related_name="events")
    event_type = models.CharField(max_length=80)
    tx_hash = models.CharField(max_length=128, db_index=True)
    ledger = models.BigIntegerField(db_index=True)
    event_index = models.IntegerField(default=0)
    topic = models.CharField(max_length=120, blank=True)
    payload = models.JSONField(default=dict)
    emitted_at = models.DateTimeField(db_index=True)

    class Meta:
        ordering = ["-ledger", "-event_index"]
        constraints = [
            models.UniqueConstraint(
                fields=["tx_hash", "event_index", "tracked_contract"],
                name="uq_event_tx_index_contract",
            )
        ]


class WebhookSubscription(TimeStampedModel):
    target_url = models.URLField()
    secret = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    event_type = models.CharField(max_length=80, blank=True)
    tracked_contract = models.ForeignKey(
        TrackedContract,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="subscriptions",
    )

    def __str__(self) -> str:
        return f"{self.target_url} ({'active' if self.is_active else 'inactive'})"
