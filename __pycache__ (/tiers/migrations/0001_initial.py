# Generated by Django 4.2.5 on 2023-09-24 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientInfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('adresse', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('actif', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Banque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('code', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('bic', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('actif', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeFournisseur', models.CharField(max_length=25)),
                ('acronym', models.CharField(max_length=150)),
                ('raison_Social', models.CharField(max_length=150)),
                ('adresse', models.CharField(default='', max_length=250)),
                ('phone', models.CharField(default='', max_length=150)),
                ('email', models.CharField(default='', max_length=150)),
                ('typefournisseur', models.CharField(choices=[('PME', 'PME'), ('Institutionnel', 'Institutionnel'), ('Automobile', 'Automobile'), ('Revendeur', 'Revendeur'), ('BTPH', 'BTPH'), ('Industrie', 'Industrie'), ('Autre', 'Autre')], default='Autre', max_length=25)),
                ('fournisseurEtrange', models.BooleanField()),
                ('fournisseurClient', models.CharField(default='', max_length=150)),
                ('store', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fournisseur_store', to='clientInfo.store')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('adresse', models.CharField(default='', max_length=250)),
                ('phone', models.CharField(default='', max_length=150)),
                ('email', models.CharField(default='', max_length=150)),
                ('ActClient', models.CharField(choices=[('Revendeur', 'revendeur'), ('Entreprise', 'entreprise')], default='Client Final', max_length=25)),
                ('registreCommerce', models.CharField(default='', max_length=150)),
                ('solde', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('categorie_client', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients_type', to='clientInfo.typeclient')),
                ('store', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_store', to='clientInfo.store')),
            ],
        ),
    ]
