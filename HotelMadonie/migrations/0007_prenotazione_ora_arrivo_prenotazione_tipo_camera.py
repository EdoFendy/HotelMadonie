# Generated by Django 4.1.7 on 2023-03-24 02:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("HotelMadonie", "0006_prenotazione_alter_hotelmadonie_titolo"),
    ]

    operations = [
        migrations.AddField(
            model_name="prenotazione",
            name="ora_arrivo",
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="prenotazione",
            name="tipo_camera",
            field=models.CharField(
                choices=[
                    ("singola", "Singola"),
                    ("doppia", "Doppia"),
                    ("tripla", "Tripla"),
                ],
                default="Singola",
                max_length=10,
            ),
        ),
    ]
