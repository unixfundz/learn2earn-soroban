from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ContractEventViewSet, TrackedContractViewSet, WebhookSubscriptionViewSet

router = DefaultRouter()
router.register("contracts", TrackedContractViewSet, basename="contracts")
router.register("events", ContractEventViewSet, basename="events")
router.register("subscriptions", WebhookSubscriptionViewSet, basename="subscriptions")

urlpatterns = [
    path("", include(router.urls)),
]
