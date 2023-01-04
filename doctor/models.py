# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class doctor(models.Model):
 name=models.CharField(max_length=200)
 about=models.TextField()
 specialist=models.CharField(max_length=200)
 location=models.CharField(max_length=200)
 price=models.DecimalField(max_digits=6,decimal_places=2)
 image=models.FileField(upload_to='photo',null=True,blank=True)
 email_recption = models.CharField(null=True,blank=True,max_length=20)
 years_of_experience = models.IntegerField(max_length=2,null=True,blank=True)
 gender = models.CharField(max_length=6,null=True,blank=True)

 def __str__(self):
  return self.name

class Bookedsession(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    data = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    email_recep = models.CharField(max_length=50)





