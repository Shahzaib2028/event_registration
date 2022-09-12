from django.contrib import admin
from .models import Events

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'date' , "location" , "owner"]
    filter_horizontal = ['attendees']

admin.site.register(Events, EventAdmin)