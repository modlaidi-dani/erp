# Generated by Django 3.2.14 on 2024-04-03 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0013_auto_20240401_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='numseries',
            name='used',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='prix_vente_kit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AddField(
            model_name='variantsprixclient',
            name='prix_vente_kit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]
