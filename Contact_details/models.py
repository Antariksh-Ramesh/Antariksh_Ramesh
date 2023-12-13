# models.py
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)  
    phone_number = models.CharField(max_length=10)

    class Meta:
        app_label = 'Contact_details'
        managed = False 

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



