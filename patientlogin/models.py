from django.db import models
from patientregister.models import pactientaccount
from medicalproviders.models import medicalproviders
# Create your models here.

class patientLogin(models.Model):
    patientdata = models.ForeignKey(pactientaccount,on_delete=models.CASCADE)
    name = models.CharField(blank=True,null=True , max_length= 10)
    
    def getEmail():
        data = list(pactientaccount.objects.values_list('email'))
        return data

    def getPassword():
        password = list(pactientaccount.objects.values_list('password'))
        return password
    
    def getID():
        password = list(pactientaccount.objects.values_list('id'))
        return password

class medicallogin(models.Model):
    medicaldata = models.ForeignKey(medicalproviders,on_delete=models.CASCADE)
    name = models.CharField(blank=True,null=True , max_length= 10)
    
    def getEmail():
        data = list(medicalproviders.objects.values_list('email'))
        return data

    def getPassword():
        password = list(medicalproviders.objects.values_list('password'))
        return password
    
    def getID():
        password = list(medicalproviders.objects.values_list('id'))
        return password