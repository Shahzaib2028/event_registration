from pyexpat import model
from django.contrib import admin
from .models import order_data

# Register your models here.


class order(admin.ModelAdmin):
    list_display = ["created_at" , "destination" ,"destination_iata" , "origin" , "origin_iata" , "type" , "departure" , "arrival"]

admin.site.register(order_data, order)