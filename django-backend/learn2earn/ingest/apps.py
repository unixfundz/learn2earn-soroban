from django.apps import AppConfig


class IngestConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ingest"

    def ready(self) -> None:
        from . import signals  # noqa: F401
