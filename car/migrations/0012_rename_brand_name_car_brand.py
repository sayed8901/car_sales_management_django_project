# Generated by Django 4.2.4 on 2024-06-08 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0011_car_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='brand_name',
            new_name='brand',
        ),
    ]
