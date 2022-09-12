from cgitb import lookup
import imp
from tkinter.tix import Tree
from django.shortcuts import render
from manage_event.serializers import EventsSerializers
from rest_framework.generics import CreateAPIView , ListAPIView , RetrieveUpdateDestroyAPIView , RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Events
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



# Create your views here.

class CreateEventAPI(CreateAPIView):

    serializer_class = EventsSerializers
    permission_classes = (IsAuthenticated,)

    def perform_create(self , serializer):
        return serializer.save(owner=self.request.user)





class RetreiveEventsAPI(ListAPIView):

    serializer_class = EventsSerializers

    def get_queryset(self):
        return Events.objects.all()




class RetreiveEventAPI(RetrieveAPIView):

    serializer_class = EventsSerializers

    def get_queryset(self):
        return (Events.objects.filter())




class UpdateDeleteAPI(RetrieveUpdateDestroyAPIView):

    serializer_class = EventsSerializers
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):

        return Events.objects.filter(owner = self.request.user)
            

class AttendAPI(APIView):
    
    # serializer_class = EventsSerializers
    permission_classes = (IsAuthenticated,)

    def post(self , request,  *args, **kwargs):
        try:
            event = Events.objects.get(pk = kwargs.get('id'))
            event.attendees.add(request.user)
            return Response ({"message" : "{username} just joined the event".format(username = request.user.username)
            , "status" : status.HTTP_201_CREATED})

        except Events.DoesNotExist:
            return Response ({"message" : "This Event doest not exist" , "status":status.HTTP_400_BAD_REQUEST})
            


    

