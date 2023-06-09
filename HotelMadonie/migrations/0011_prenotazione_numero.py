# Generated by Django 4.1.7 on 2023-03-24 20:44

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("HotelMadonie", "0010_prenotazione_email_alter_prenotazione_tipo_camera"),
    ]

    operations = [
        migrations.AddField(
            model_name="prenotazione",
            name="numero",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, region=None
            ),
        ),
    ]
