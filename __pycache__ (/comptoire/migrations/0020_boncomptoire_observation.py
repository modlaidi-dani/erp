# Generated by Django 3.2.14 on 2024-02-25 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comptoire', '0019_alter_affectationcaisse_emplacement'),
    ]

    operations = [
        migrations.AddField(
            model_name='boncomptoire',
            name='observation',
            field=models.CharField(blank=True, default='', max_length=4500, null=True),
        ),
    ]
