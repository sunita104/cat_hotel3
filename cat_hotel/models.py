from django.db import models
from django.utils import timezone
# Create your models here.

class Room(models.Model):
    number_room = models.CharField(max_length=50, primary_key=True)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.number_room

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    cat = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)

