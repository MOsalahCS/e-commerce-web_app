# Generated by Django 4.1.3 on 2023-08-23 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_orders_payment_status_orders_total_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='total_amount',
        ),
    ]
