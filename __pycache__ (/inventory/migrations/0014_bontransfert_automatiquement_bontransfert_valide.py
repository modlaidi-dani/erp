# Generated by Django 4.2.5 on 2023-10-08 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_bonreintegration_produitsenbonreintegration'),
    ]

    operations = [
        migrations.AddField(
            model_name='bontransfert',
            name='automatiquement',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='bontransfert',
            name='valide',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
