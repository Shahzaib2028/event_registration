from rest_framework import serializers
from manage_event.models import Events

class EventsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ("id" ,"title" , "description" , "date" , "location")

