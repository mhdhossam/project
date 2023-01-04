# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import OrderedDict
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from patientregister.models import pactientaccount
from doctor.models import doctor


def Home(request):
   data = doctor.objects.all()
   listt = []
   for e in data:
      listt.append(e.specialist)
   listt = list(set(listt))
   return render(request,'Home/Home.html',{'rs2':listt})
