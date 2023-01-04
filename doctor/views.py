# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import doctor
# Create your views here.
# def doctor_profile(request,em_rec):
#     doctorw=doctor.objects.get(email_recep = em_rec)
#     return render(request,'doctor profile/dr-profile.html',{'doctor':doctorw,'dd':em_rec})

# def doctor_profile_RE(request,email,em_rec):
#     doctorw=doctor.objects.get(email_recep = em_rec)
#     return render(request,'doctor profile/dr-profile.html',{'doctor':doctorw,'dd':em_rec,'rs':email})