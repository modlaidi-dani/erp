# Generated by Django 4.2.5 on 2023-10-15 05:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("tiers", "0006_remove_client_actclient"),
        ("ventes", "0010_alter_facture_mode_reglement"),
    ]

    operations = [
        migrations.CreateModel(
            name="AvoirVente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codeAvoir", models.CharField(max_length=200)),
                ("dateEmission", models.DateField(default=datetime.datetime.now)),
                ("motif", models.CharField(max_length=200)),
                (
                    "BonSortieAssocie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="avoirs_bonsortie",
                        to="ventes.bonsortie",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="avoirs_client",
                        to="tiers.client",
                    ),
                ),
            ],
        ),
    ]
