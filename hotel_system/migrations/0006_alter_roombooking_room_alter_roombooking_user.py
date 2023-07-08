# Generated by Django 4.1.2 on 2023-06-05 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel_system', '0005_alter_roombooking_room_alter_roombooking_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roombooking',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel_system.room'),
        ),
        migrations.AlterField(
            model_name='roombooking',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]