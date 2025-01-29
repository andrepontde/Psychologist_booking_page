from django.db import models

# Create your models here.

#I want a user table to hold info about the person that did the booking to begin with!!! - it would also connect with the psytest table

#Booking table definition
class booking(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
