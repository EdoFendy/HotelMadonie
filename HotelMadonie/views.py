from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.shortcuts import render, redirect
from .models import HotelMadonie, Prenotazione 
from .forms import PrenotazioneForm, CreateUserForm





def registerPage(request):
    form = CreateUserForm()
    logo = HotelMadonie.objects.get(titolo='Logo')
    sfondo2 = HotelMadonie.objects.get(titolo='Sfondo2')
    context = {'form' : form, 'logo' : logo.immagine, 'sfondo2' : sfondo2.immagine}
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'HotelMadonie/register.html', context)

def hotel_paradiso(request):
    immagini = ['Logo', 'Sfondo', 'Sfondo2', 'Colazione', 'Reception2', 'Reception']

    context = {}
    for immagine in immagini:
        oggetto = HotelMadonie.objects.get(titolo=immagine)
        context[immagine.lower()] = oggetto.immagine

    
    return render(request, 'HotelMadonie/HotelParadiso.html', context)

def Castelbuono(request):
    logo = HotelMadonie.objects.get(titolo='Logo')
    sfondo = HotelMadonie.objects.get(titolo='Sfondo')
    sfondo2 = HotelMadonie.objects.get(titolo='Sfondo2')
    castello = HotelMadonie.objects.get(titolo='Castello')
    manna = HotelMadonie.objects.get(titolo='Manna')
    fiasconaro = HotelMadonie.objects.get(titolo='Fiasconaro')
    parcomadonie = HotelMadonie.objects.get(titolo='Parcomadonie')
    context = {
                'logo': logo.immagine,
                'sfondo': sfondo.immagine,
                'castello' : castello.immagine,
                'manna' : manna.immagine,
                'fiasconaro' : fiasconaro.immagine,
                'parcomadonie' : parcomadonie.immagine, 'sfondo2': sfondo2.immagine
               }
    return render(request, 'HotelMadonie/Castelbuono.html', context)

def Camere(request):
    logo = HotelMadonie.objects.get(titolo='Logo')
    sfondo = HotelMadonie.objects.get(titolo='Sfondo')
    sfondo2 = HotelMadonie.objects.get(titolo='Sfondo2')
    fronte = HotelMadonie.objects.get(titolo='Fronte')
    reception2 = HotelMadonie.objects.get(titolo='Reception2')
    reception = HotelMadonie.objects.get(titolo='Reception')
    corridoio = HotelMadonie.objects.get(titolo='Corridoio')
    camera2 = HotelMadonie.objects.get(titolo='Camera2')
    camera = HotelMadonie.objects.get(titolo='Camera')
    bagno = HotelMadonie.objects.get(titolo='Bagno')
    camerabella = HotelMadonie.objects.get(titolo='CameraBella')
    camerabella2 = HotelMadonie.objects.get(titolo='CameraBella2')
    camerabella3 = HotelMadonie.objects.get(titolo='CameraBella3')
    porta = HotelMadonie.objects.get(titolo='PortaCamere')
    hotel1 = HotelMadonie.objects.get(titolo='Hotel1')
    scala = HotelMadonie.objects.get(titolo='Scala')
    
    context = {
                'logo': logo.immagine,
                'sfondo': sfondo.immagine,
                'fronte': fronte.immagine,
                'reception2': reception2.immagine,
                'reception': reception.immagine,
                'corridoio': corridoio.immagine,
                'camera2': camera2.immagine,
                'camera': camera.immagine,
                'bagno': bagno.immagine,
                'camerabella': camerabella.immagine,
                'camerabella2': camerabella2.immagine,
                'camerabella3': camerabella3.immagine,
                'porta': porta.immagine,
                'hotel1': hotel1.immagine,
                'sfondo2': sfondo2.immagine,
                'scala': scala.immagine,

                }

    return render(request, 'HotelMadonie/Camere.html', context)


class PrenotazioniListView(ListView):
    model = Prenotazione
    template_name = 'HotelMadonie/prenotazioni.html'
    context_object_name = 'prenotazioni'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logo = HotelMadonie.objects.get(titolo='Logo')
        sfondo2 = HotelMadonie.objects.get(titolo='Sfondo2')
        context['logo'] = logo.immagine
        context['sfondo2'] = sfondo2.immagine
        return context

class NuovaPrenotazioneView(CreateView):
    model = Prenotazione
    form_class = PrenotazioneForm
    template_name = 'HotelMadonie/NuovaPrenotazione.html'
    success_url = reverse_lazy('HotelMadonie:nuova_prenotazione')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logo = HotelMadonie.objects.get(titolo='Logo')
        sfondo2 = HotelMadonie.objects.get(titolo='Sfondo2')
        context['logo'] = logo.immagine
        context['sfondo2'] = sfondo2.immagine
        return context
    def get_success_url(self):
        return self.request.path

class PrenotazioneDeleteView(DeleteView):
    model = Prenotazione
    template_name = 'HotelMadonie/elimina_prenotazione.html'
    success_url = reverse_lazy('prenotazioni')
      


def Contattaci(request):
    immagini = ['Logo', 'Sfondo2']

    context = {}
    for immagine in immagini:
        oggetto = HotelMadonie.objects.get(titolo=immagine)
        context[immagine.lower()] = oggetto.immagine

    
    return render(request, 'HotelMadonie/Contattaci.html', context)

class PrenotazioneUpdateView(UpdateView):
    model = Prenotazione
    fields = ['tipo_camera', 'nome', 'cognome', 'email', 'numero', 'data_arrivo', 'data_partenza', 'ora_arrivo', 'num_camere']
    template_name = 'HotelMadonie/modifica_prenotazione.html'

    def get_success_url(self):
        return reverse_lazy('prenotazioni')
        