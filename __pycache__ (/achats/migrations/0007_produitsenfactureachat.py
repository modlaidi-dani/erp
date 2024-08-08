# Generated by Django 4.2.5 on 2023-10-08 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0005_verificationarchive_entrepot'),
        ('achats', '0006_bonreception_produitsenbonreception_factureachat'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProduitsEnFactureAchat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('unitprice', models.DecimalField(decimal_places=2, default=0, max_digits=15, null=True)),
                ('totalprice', models.DecimalField(decimal_places=2, default=0, max_digits=15, null=True)),
                ('FactureNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produits_en_factureachats', to='achats.factureachat')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factures_achat', to='produits.product')),
            ],
        ),
    ]
