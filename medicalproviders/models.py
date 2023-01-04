from __future__ import unicode_literals
from django.db import models


class medicalproviders(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    age = models.IntegerField()
    mobilenumber = models.IntegerField(unique=True)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    confirmpassword = models.CharField(max_length=50)
    NationalId=models.IntegerField()
    choosemedicalprovider=models.CharField(max_length=50)

    def __str__(self):
     return self.first_name


# Create your models here.
