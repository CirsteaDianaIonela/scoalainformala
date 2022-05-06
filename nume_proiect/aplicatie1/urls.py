#vom pune url-urile secundare ale aplicatiei
from django.urls import path

from aplicatie1 import views

app_name = 'locations'

urllpatterns = [

    path('', views.LocationsView.as_view(), name = 'lista_locatii'),
]