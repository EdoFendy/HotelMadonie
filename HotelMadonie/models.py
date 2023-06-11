import datetime
from django.db import models

class HotelMadonie(models.Model):
    immagine = models.ImageField()
    titolo = models.TextField(max_length=20)
    
    def __str__(self):
        return self.titolo

class Prenotazione(models.Model):
    TIPI_CAMERA = [
        ('Singola', 'Singola'),
        ('Doppia', 'Doppia'),
        ('Tripla', 'Tripla'),
    ]
    tipo_camera = models.CharField(max_length=100, choices=TIPI_CAMERA)
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    email = models.EmailField(default='')
    numero = models.CharField(max_length=15)
    data_arrivo = models.DateField()
    data_partenza = models.DateField()
    ora_arrivo = models.TimeField()
    num_camere = models.IntegerField()

    def __str__(self):
        return f"{self.nome} {self.cognome}"


