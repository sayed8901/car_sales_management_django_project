# Generated by Django 5.0.6 on 2024-06-09 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0015_car_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='customer',
        ),
        migrations.AddField(
            model_name='car',
            name='customer',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
