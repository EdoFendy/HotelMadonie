from django import forms
from .models import Prenotazione
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

def send_confirmation_email(prenotazione):
    subject = 'Conferma Prenotazione'
    message = f'Ciao {prenotazione.nome},\n\n Grazie per aver prenotato con noi! Questa è una conferma della tua prenotazione.\n\nData di arrivo: {prenotazione.data_arrivo}\nData di partenza: {prenotazione.data_partenza}\n\nGrazie per aver scelto il nostro hotel!\n'
    from_email = 'massatria@libero.it'
    recipient_list = [prenotazione.email]
    send_mail(subject, message, from_email, recipient_list)

class PrenotazioneForm(forms.ModelForm):
    class Meta:
        model = Prenotazione
        fields = '__all__'

    def save(self, commit=True):
        prenotazione = super().save(commit=False)
        if commit:
            prenotazione.save()
            send_confirmation_email(prenotazione)
        return prenotazione