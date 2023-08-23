# Generated by Django 4.2.4 on 2023-08-23 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('P', 'pending'), ('C', 'completed')], default='P', max_length=1),
        ),
    ]