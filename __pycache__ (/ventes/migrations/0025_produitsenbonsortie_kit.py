# Generated by Django 4.2.5 on 2024-07-08 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventes', '0024_alter_bonsortie_etat_reglement'),
    ]

    operations = [
        migrations.AddField(
            model_name='produitsenbonsortie',
            name='kit',
            field=models.TextField(default=''),
        ),
    ]
