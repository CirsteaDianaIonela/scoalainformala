#vom pune url-urile secundare ale aplicatiei
from django.urls import path, include

from aplicatie1 import views

app_name = 'locations'

urlpatterns = [

    path('', views.LocationsView.as_view(), name='lista_locatii'),
    path('adaugare/', views.CreateLocationView.as_view(), name='adauga'),
    path('<int:pk>/update/', views.UpdateLocationView.as_view(), name='modifica'),
    path('<int:pk>/delete/', views.delete_location, name='sterge'),
    path('locatii_inactive', views.LocationInactiveView.as_view(), name='locatii_inactive'),
    path('<int:pk>/activeaza/', views.activate_location, name='activeaza'),


]
