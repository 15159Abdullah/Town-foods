# Generated by Django 4.1.2 on 2023-06-05 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel_system', '0004_alter_roombooking_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roombooking',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotel_system.room'),
        ),
        migrations.AlterField(
            model_name='roombooking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
