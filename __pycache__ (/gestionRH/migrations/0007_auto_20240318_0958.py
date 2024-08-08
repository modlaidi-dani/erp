# Generated by Django 3.2.14 on 2024-03-18 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionRH', '0006_primemotivation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='renumeration',
            name='date_arrive',
        ),
        migrations.RemoveField(
            model_name='renumeration',
            name='salaire_declare',
        ),
        migrations.RemoveField(
            model_name='renumeration',
            name='salaire_espece',
        ),
        migrations.AddField(
            model_name='primemotivation',
            name='viremenet',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='renumeration',
            name='mois',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='renumeration',
            name='virement_valide',
            field=models.BooleanField(default=False),
        ),
    ]
