# Generated by Django 4.2.5 on 2023-09-25 14:22

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('reglements', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReglementsCustomPermission',
            fields=[
                ('permission_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.permission')),
            ],
            options={
                'verbose_name': 'Custom Permission',
                'verbose_name_plural': 'Custom Permissions',
            },
            bases=('auth.permission',),
            managers=[
                ('objects', django.contrib.auth.models.PermissionManager()),
            ],
        ),
    ]
