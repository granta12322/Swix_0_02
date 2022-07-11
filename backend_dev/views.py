from django.shortcuts import render
from rest_framework.response import  Response # Response object takes data in database and renders as json db.
from rest_framework.decorators import api_view, action
from rest_framework import generics, viewsets 
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.reverse import reverse
from django.shortcuts import get_object_or_404, render

from .serializers import EventSerializer, VenueSerializer, TicketSerializer
from .models import Event, Venue, Ticket
# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users-list', request=request, format=format),
        'events': reverse('events-list', request=request, format=format),
        'organisers': reverse('organisers-list', request=request, format=format),
        'acts': reverse('acts-list', request=request, format=format),
        'venues': reverse('venues-list', request=request, format=format),
        'genres': reverse('genres-list', request=request, format=format),
        'tickets': reverse('tickets-list', request=request, format=format),
    })



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def list(self,request):    
        serializer = EventSerializer(self.queryset,many = True, context = {'request': request})
        return Response(serializer.data)
    
    def retrieve(self,request, pk):
        print("Got here first")
        event = get_object_or_404(self.queryset, pk = pk)
        print("Got here")
        serializer = EventSerializer(event,many = False, context = {'request': request})
        print(request.data)
        return Response(serializer.data)
    
    def perform_create(self,request):
        print(request)
        serializer = EventSerializer(data = request.data, context = {'request': request})
        print("C")
        if serializer.is_valid():
            print("D")
            print(self.request.user)
            serializer.save(organiser = self.request.user)
            print("E")
            return Response(status=200)
        return Response(Status=404)     # !!! Shouldn't be a status 404, should be something else


    @action(detail = True, methods = ['post','get'])
    def generate_tickets(self,request, pk):
        print("Generating Tickets")
        print("Ticket number:")
        ticket_number = int(request.query_params.get('ticket_number'))

        #print(request.__dict__)
        event = get_object_or_404(self.queryset, pk = pk)
        

        print("Serializer valid, looping")

        for i in range(ticket_number):
            print("Ticket Saved", i)
            Ticket(event = event, owner = event.organiser).save()

        return Response(status=200)




class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

    def list(self,request):    
        serializer = VenueSerializer(self.queryset,many = True, context = {'request': request})
        return Response(serializer.data)
    
    def retrieve(self,request, pk):
        venue = get_object_or_404(self.queryset, pk = pk)
        serializer = VenueSerializer(venue,many = False, context = {'request': request})
        return Response(serializer.data)
    
    def perform_create(self,request):
        print(request)
        serializer = VenueSerializer(data = request.data, context = {'request': request})
        print("C")
        if serializer.is_valid():
            print("D")
            serializer.save()  #organiser = self.request.user)
            print("E")
            return Response(status=200)
        return Response(Status=404)     # !!! Shouldn't be a status 404, should be something else


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def list(self,request):    
        serializer = TicketSerializer(self.queryset,many = True, context = {'request': request})
        return Response(serializer.data)
    
    def retrieve(self,request, pk):
        ticket = get_object_or_404(self.queryset, pk = pk)
        serializer = TicketSerializer(ticket,many = False, context = {'request': request})
        return Response(serializer.data)


    

    

