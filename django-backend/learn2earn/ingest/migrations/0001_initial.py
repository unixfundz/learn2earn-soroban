from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TrackedContract",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("contract_id", models.CharField(max_length=128, unique=True)),
                ("label", models.CharField(blank=True, max_length=120)),
                ("is_active", models.BooleanField(default=True)),
                ("start_ledger", models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="WebhookSubscription",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("target_url", models.URLField()),
                ("secret", models.CharField(max_length=128)),
                ("is_active", models.BooleanField(default=True)),
                ("event_type", models.CharField(blank=True, max_length=80)),
                (
                    "tracked_contract",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscriptions",
                        to="ingest.trackedcontract",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ContractEvent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("event_type", models.CharField(max_length=80)),
                ("tx_hash", models.CharField(db_index=True, max_length=128)),
                ("ledger", models.BigIntegerField(db_index=True)),
                ("event_index", models.IntegerField(default=0)),
                ("topic", models.CharField(blank=True, max_length=120)),
                ("payload", models.JSONField(default=dict)),
                ("emitted_at", models.DateTimeField(db_index=True)),
                (
                    "tracked_contract",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="events", to="ingest.trackedcontract"),
                ),
            ],
            options={"ordering": ["-ledger", "-event_index"]},
        ),
        migrations.AddConstraint(
            model_name="contractevent",
            constraint=models.UniqueConstraint(
                fields=("tx_hash", "event_index", "tracked_contract"),
                name="uq_event_tx_index_contract",
            ),
        ),
    ]
