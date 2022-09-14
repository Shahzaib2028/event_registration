from statistics import mode
from django.db import models

# Create your models here.

class order_data(models.Model):
    created_at = models.DateTimeField()
    destination = models.CharField(max_length=150)
    destination_iata = models.CharField(max_length=50)
    origin = models.CharField(max_length=150)
    origin_iata = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()

    def __str__(self):
        return str(self.id)