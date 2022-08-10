from rest_framework import serializers
from .models import Event, Ticket, Venue

class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(view_name= 'venue-detail', many = False, read_only = False, lookup_field="pk", queryset = Venue.objects.all())
    tickets = serializers.HyperlinkedRelatedField(view_name = 'ticket-detail', many = True, read_only = True )
    
    class Meta:
        model = Event
        fields = ['name','creation_date','start_datetime','venue', 'tickets']

class VenueSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(view_name= 'event-detail', many = True, read_only = True)

    class Meta:
        model = Venue
        fields = ['name','address','events']


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.HyperlinkedRelatedField(view_name = 'event-detail', many = False, read_only = True)

    class Meta:
        model = Ticket
        fields = ['owner','event']
        



