from attr import field
from rest_framework import serializers
from .models import Event, Venue

class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(view_name= 'venue-detail', many = False, read_only = True)

    class Meta:
        model = Event
        fields = ['name','creation_date','start_datetime','venue']

class VenueSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(view_name= 'event-list', many = True, read_only = True)

    class Meta:
        model = Venue
        fields = ['name','address']

