# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
 
from django.shortcuts import render,redirect
from .models import pactientaccount



def signup(request):
   
   first_name=request.POST.get('first_name')
   last_name = request.POST.get('last_name')
   
   
   
   age = request.POST.get('age')
   mobilenumber = request.POST.get('mobilenumber')
   address = request.POST.get('address')
   email = request.POST.get('email')
   password = request.POST.get('password')
   confirmpassword = request.POST.get('confirmpassword')
   NationalId=request.POST.get('NationalId')
   
   
   
   data=pactientaccount(
   first_name=first_name,
   last_name=last_name,

   gender= request.POST.get('gender'),
      
    
    
   age=age,
   mobilenumber=mobilenumber,
   address=address,
   email=email,
   password=password,
   confirmpassword=confirmpassword,
   NationalId=NationalId,
   )
   
   if request.method=='POST':
    data.save()
    return render(request,'Home/Home.html')
   return render(request,'Regstration/index.html')
 
