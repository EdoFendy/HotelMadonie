# Generated by Django 4.1.7 on 2023-05-03 18:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("HotelMadonie", "0012_alter_prenotazione_numero"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="prenotazione",
            name="num_ospiti",
        ),
    ]