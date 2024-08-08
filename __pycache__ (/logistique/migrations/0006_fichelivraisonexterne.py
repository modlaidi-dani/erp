# Generated by Django 4.2.5 on 2024-03-27 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistique', '0005_blsenrequeteclient_delete_blsenrequete'),
    ]

    operations = [
        migrations.CreateModel(
            name='FicheLivraisonExterne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('adresse', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('transporteur', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('modePaiement', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('montant', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('numeroColis', models.IntegerField(default=1)),
                ('note', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
    ]
