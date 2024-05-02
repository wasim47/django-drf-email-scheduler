from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=150)
    contact = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    date_of_birth = models.DateField()
