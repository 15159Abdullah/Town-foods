# Generated by Django 4.1.2 on 2023-06-05 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_system', '0009_invoices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoices',
            name='inv_no',
        ),
    ]
