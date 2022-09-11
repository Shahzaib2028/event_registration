from operator import mod
from pyexpat import model
from tkinter import CASCADE
from turtle import title
from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User


# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=500)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
 
    def __str__(self):
        return self.title