# Generated by Django 5.0.4 on 2024-05-19 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_car_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='customer',
        ),
    ]
