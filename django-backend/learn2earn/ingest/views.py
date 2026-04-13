from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import ContractEvent, TrackedContract, WebhookSubscription
from .serializers import ContractEventSerializer, TrackedContractSerializer, WebhookSubscriptionSerializer


class TrackedContractViewSet(viewsets.ModelViewSet):
    queryset = TrackedContract.objects.all().order_by("-created_at")
    serializer_class = TrackedContractSerializer
    permission_classes = [AllowAny]
    filterset_fields = ["is_active", "contract_id"]


class ContractEventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContractEvent.objects.select_related("tracked_contract").all()
    serializer_class = ContractEventSerializer
    permission_classes = [AllowAny]
    filterset_fields = ["event_type", "ledger", "tracked_contract__contract_id", "tx_hash"]


class WebhookSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = WebhookSubscription.objects.select_related("tracked_contract").all().order_by("-created_at")
    serializer_class = WebhookSubscriptionSerializer
    permission_classes = [AllowAny]
    filterset_fields = ["is_active", "event_type", "tracked_contract__contract_id"]
