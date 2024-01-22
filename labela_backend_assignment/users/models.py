from django.db import models

class User(models.Model):
    
    fullName = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)

   
