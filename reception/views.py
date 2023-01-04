# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import pandas as pd
from patientregister.models import pactientaccount
from medicalproviders.models import medicalproviders
from doctor.models import doctor , Bookedsession

# Create your views here.

def reception(request,email):
    data1 = 'patient'
    bookedse =[]
    data = pactientaccount.objects.filter(mobilenumber=email)
    if data :
        name = data[0].mobilenumber
    else:
        data1 = medicalproviders.objects.filter(mobilenumber=email)
        data1 = data1[0].choosemedicalprovider
        data = medicalproviders.objects.filter(mobilenumber=email)
        name = data[0].mobilenumber
        dataaa = medicalproviders.objects.filter(mobilenumber=email)
        bookedse =[]
        bookedsed = list(Bookedsession.objects.filter(email_recep =dataaa[0].email ))
        for e in bookedsed:
            bookedse.append(e)
        
    return render(request,'reception/index.html',{'doctor':data[0] ,'medical':data1,'rs':email , 'email_res':data[0].email,'bookedse':bookedse})