from cgitb import lookup
import imp
from django.shortcuts import render
from manage_event.serializers import EventsSerializers
from rest_framework.generics import CreateAPIView , ListAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Events
from rest_framework.views import APIView
from rest_framework.response import Response
# from core.permissions import IsOwner


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




# class RetreiveEventAPI(APIView):

#     def get(self , request,  pk=None , format = None):
#         id = pk

#         if id is not None:
#             event = Events.objects.get(id=id)
#             serializers = EventsSerializers(event)
#             return Response(serializers.data)


class UpdateDeleteAPI(RetrieveUpdateDestroyAPIView):

    serializer_class = EventsSerializers
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Events.objects.filter(owner = self.request.user)
    

