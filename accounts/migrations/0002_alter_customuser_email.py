# Generated by Django 4.1.2 on 2023-06-01 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default=True, max_length=254, unique=True),
        ),
    ]