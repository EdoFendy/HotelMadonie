from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import PrenotazioneDeleteView, PrenotazioneUpdateView, NuovaPrenotazioneView

urlpatterns = [
    path("", views.hotel_paradiso, name="Home"),
    path("Castelbuono/", views.Castelbuono, name="Castelbuono"),
    path("Camere/", views.Camere, name="Camere"),
    path("Contattaci/", views.Contattaci, name="Contattaci"),
    path('prenotazioni/', views.PrenotazioniListView.as_view(), name='prenotazioni'),
    path('prenotazioni/<int:pk>/elimina/', PrenotazioneDeleteView.as_view(), name='elimina_prenotazione'),
    path('nuova_prenotazione/', NuovaPrenotazioneView.as_view(), name='nuova_prenotazione'),
    path('<int:pk>/modifica/', PrenotazioneUpdateView.as_view(), name='modifica_prenotazione'),
    path('register/', views.registerPage, name='register')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)