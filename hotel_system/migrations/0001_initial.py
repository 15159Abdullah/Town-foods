# Generated by Django 4.1.2 on 2023-06-01 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Resto_menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_price', models.CharField(max_length=50)),
                ('item_img', models.ImageField(upload_to='Menu_img/')),
                ('item_description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(choices=[('Family Room', 'Family Room'), ('Deluxe Room', 'Deluxe Room'), ('Classic Room', 'Classic Room'), ('Superior Room', 'Superior Room'), ('Luxury Room', 'Luxury Room'), ('Suite Room', 'Suite Room')], max_length=13)),
                ('room_number', models.IntegerField(default=True, unique=True)),
                ('room_bed_quantity', models.IntegerField(default=True)),
                ('room_image', models.ImageField(blank=True, upload_to='room_pictures/')),
                ('room_price', models.IntegerField(default=True)),
                ('room_capacity', models.IntegerField(default=True)),
                ('room_is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=100)),
                ('booking_price', models.IntegerField(default=True)),
                ('booked_room_number', models.IntegerField(default=True)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_system.room')),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
