# Generated by Django 5.1.3 on 2024-11-26 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_shippingaddress_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopper',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=90),
        ),
    ]
