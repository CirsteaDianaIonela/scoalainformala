from rest_framework import viewsets

from aplicatie1.models import Locations
from myapi.serializers import LocationSerializers


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Locations.objects.all().order_by('city')
    serializer_class = LocationSerializers