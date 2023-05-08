# Generated by Django 4.2 on 2023-05-07 17:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0003_booking_booking_slot"),
    ]

    operations = [
        migrations.CreateModel(
            name="MenuCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=125)),
            ],
        ),
    ]
