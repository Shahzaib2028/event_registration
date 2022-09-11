from django.contrib import admin
from .models import Events

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date' , "location" , "owner")

admin.site.register(Events, EventAdmin)