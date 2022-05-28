from rest_framework import serializers

from aplicatie1.models import Locations


class LocationSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Locations
        fields = ['city', 'country']
