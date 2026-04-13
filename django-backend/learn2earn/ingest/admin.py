from django.contrib import admin
from .models import TrackedContract, ContractEvent, WebhookSubscription


@admin.register(TrackedContract)
class TrackedContractAdmin(admin.ModelAdmin):
    list_display = ("contract_id", "label", "is_active", "start_ledger")
    search_fields = ("contract_id", "label")


@admin.register(ContractEvent)
class ContractEventAdmin(admin.ModelAdmin):
    list_display = ("tracked_contract", "event_type", "ledger", "tx_hash", "event_index", "emitted_at")
    list_filter = ("event_type", "tracked_contract")
    search_fields = ("tx_hash", "tracked_contract__contract_id")


@admin.register(WebhookSubscription)
class WebhookSubscriptionAdmin(admin.ModelAdmin):
    list_display = ("target_url", "event_type", "tracked_contract", "is_active")
    list_filter = ("is_active", "event_type")
