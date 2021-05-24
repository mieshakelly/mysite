from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Client(models.Model):
   client_name = models.CharField(max_length=251)
   address = models.CharField(max_length=251)
   pub_date = models.DateTimeField('date published')

   def __str__(self):
       return self.client_name

class Pet(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default='')
    pet_name = models.CharField(max_length=251)
    description = models.CharField(max_length=501)

    def __str__(self):
        return self.pet_name
