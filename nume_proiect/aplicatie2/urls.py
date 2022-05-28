#vom pune url-urile secundare ale aplicatiei
from django.urls import path

from aplicatie2 import views

app_name = 'companies'

urlpatterns = [

    path('', views.CompanyView.as_view(), name='listare'),
    path('adaugare/', views.CreateCompanyView.as_view(), name='add'),
    path('<int:pk>/update/', views.UpdateCompanyView.as_view(), name='modifica'),
    path('<int:pk>/delete/', views.delete_companies, name='sterge'),
    path('companii_inactive', views.CompaniesInactiveView.as_view(), name='companii_inactive'),
    path('<int:pk>/activeaza/', views.activate_companies, name='activeaza'),

]
