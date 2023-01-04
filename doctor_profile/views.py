# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from doctor.models import doctor
from django.http import HttpResponse
from medicalproviders.models import medicalproviders
# Create your views here.

def profile(request,email,email_res):
    medical = medicalproviders.objects.filter(mobilenumber=email)
    medical = medical[0].choosemedicalprovider
    doctordata = doctor.objects.get(email_recption = email_res)
    if request.POST.get('save'):
      name = request.POST.get('name')
      about = request.POST.get('about')
      specialist = request.POST.get('specialist')
      location = request.POST.get('location')
      price = request.POST.get('price')
      years_of_experience = request.POST.get('years_of_experience')
      gender = request.POST.get('gender')
      cover = request.POST.get('cover')
      data = doctor(name=name,about=about,specialist=specialist,image = cover, location=location, price=price,email_recption = email_res, years_of_experience=years_of_experience, gender=gender)
      if request.method == 'POST':
         data.save()
    elif request.POST.get('update'):
       name = request.POST.get('name')
       about = request.POST.get('about')
       specialist = request.POST.get('specialist')
       location = request.POST.get('location')
       price = request.POST.get('price')
       years_of_experience = request.POST.get('years_of_experience')
       gender = request.POST.get('gender')
       
       doctordata.name = name
       doctordata.about = about
       doctordata.specialist = specialist
       doctordata.location = location
       doctordata.price = price
       doctordata.years_of_experience = years_of_experience
       doctordata.gender = gender
       if request.method == 'POST':
         doctordata.save()

       return render(request, 'profile/profile.html',{'rs':email , 'email_res':email_res,'medical':medical, 'data':doctordata})
    return render(request, 'profile/profile.html',{'rs':email,'email_res':email_res,'medical':medical, 'data':doctordata})










