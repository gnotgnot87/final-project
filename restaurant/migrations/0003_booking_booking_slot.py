# Generated by Django 4.2 on 2023-05-07 16:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "restaurant",
            "0002_alter_booking_guests_count_alter_menu_inventory",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="booking_slot",
            field=models.SmallIntegerField(default=10),
        ),
    ]