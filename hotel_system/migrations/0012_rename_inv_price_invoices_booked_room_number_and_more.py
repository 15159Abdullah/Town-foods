# Generated by Django 4.1.2 on 2023-06-08 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel_system', '0011_invoices_inv_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoices',
            old_name='inv_price',
            new_name='booked_room_number',
        ),
        migrations.RenameField(
            model_name='invoices',
            old_name='inv_room_no',
            new_name='booking_price',
        ),
        migrations.RenameField(
            model_name='invoices',
            old_name='Inv_check_out_date',
            new_name='check_in_date',
        ),
        migrations.RenameField(
            model_name='invoices',
            old_name='inv_check_in_date',
            new_name='check_out_date',
        ),
        migrations.RenameField(
            model_name='invoices',
            old_name='inv_room_name',
            new_name='guest_name',
        ),
        migrations.RemoveField(
            model_name='invoices',
            name='inv_user_email',
        ),
        migrations.RemoveField(
            model_name='invoices',
            name='inv_user_name',
        ),
        migrations.AddField(
            model_name='invoices',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel_system.room'),
        ),
        migrations.AddField(
            model_name='invoices',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
