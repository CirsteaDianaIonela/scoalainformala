from django.urls import path, include
from rest_framework import routers

from myapi import views #pt ca fac referire la fisierul de views.py

router = routers.DefaultRouter()
router.register('location', views.LocationViewSet)

urlpatterns = [
    path('', include(router.urls))

]