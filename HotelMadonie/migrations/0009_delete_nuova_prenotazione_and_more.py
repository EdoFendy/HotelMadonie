# Generated by Django 4.1.7 on 2023-03-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("HotelMadonie", "0008_nuova_prenotazione"),
    ]

    operations = [
        migrations.DeleteModel(
            name="nuova_prenotazione",
        ),
        migrations.RemoveField(
            model_name="prenotazione",
            name="prezzo_totale",
        ),
        migrations.AlterField(
            model_name="prenotazione",
            name="cognome",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="prenotazione",
            name="nome",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="prenotazione",
            name="ora_arrivo",
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name="prenotazione",
            name="tipo_camera",
            field=models.CharField(max_length=100),
        ),
    ]
