# Generated by Django 4.1.2 on 2023-06-05 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel_system', '0003_alter_room_room_bed_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roombooking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
