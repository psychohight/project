# Generated by Django 5.1.3 on 2024-11-25 16:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_shopper_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address_1', models.CharField(help_text='adresse et numero', max_length=1024)),
                ('address_2', models.CharField(blank=True, help_text='batiment, etages,...', max_length=1024)),
                ('city', models.CharField(max_length=1024)),
                ('zip_code', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
