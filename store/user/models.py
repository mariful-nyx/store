from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    options = [
        ('CUSTOMER', 'Customer'),
        ('RETAILER', 'Retailer')
    ]
    role = models.CharField(max_length=255, choices=options)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=550, blank=True, null=True)

    def __str__(self):
        return self.username