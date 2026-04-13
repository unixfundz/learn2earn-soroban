from rest_framework import serializers
from .models import ContractEvent, TrackedContract, WebhookSubscription


class TrackedContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackedContract
        fields = "__all__"


class ContractEventSerializer(serializers.ModelSerializer):
    contract_id = serializers.CharField(source="tracked_contract.contract_id", read_only=True)

    class Meta:
        model = ContractEvent
        fields = "__all__"


class WebhookSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookSubscription
        fields = "__all__"
        extra_kwargs = {"secret": {"write_only": True}}
