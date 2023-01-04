# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import datetime ,time
from medicalproviders.models import medicalproviders
#
from .check import checkData
from.check import checkData1
from django.shortcuts import render
from .models import patientLogin,medicallogin
from patientregister.models import pactientaccount
from doctor.models import doctor , Bookedsession

#homeuser
def homeuser(request,email ):
  data = pactientaccount.objects.filter(mobilenumber=email)
  if data :
    name = data[0].mobilenumber
  else:
    data = medicalproviders.objects.filter(mobilenumber=email)
    name = data[0].mobilenumber
  data = doctor.objects.all()
  listt = []
  for e in data:
    listt.append(e.specialist)
  listt = list(set(listt))
  return render(request,'Home/Home.html',{'rs':name,'rs2':listt})


#card and spectialist
def cards(request,email):
  data = doctor.objects.all()
  data1 = pactientaccount.objects.filter(mobilenumber=email)
  if data1 :
    name = data1[0].mobilenumber
  else:
    data1 = medicalproviders.objects.filter(mobilenumber=email)
    name = data1[0].mobilenumber
  em_rec=data[0].email_recption

  name = data1[0].first_name + data1[0].last_name
  phone = data1[0].mobilenumber
  date = datetime.today()
  timming = time.hour
  data1 = Bookedsession(name=name , phone = phone ,email_recep = em_rec)
  if request.POST:
      data1.save()
  return render(request,'Specialtais/Specialtais.html',{'rs':email,'rs2':data})

def cardsUnRe(request):
  data = doctor.objects.all()
  return render(request,'Specialtais/Specialtais.html',{'rs2':data})

def sprcialCard(request,email,data):
  data = doctor.objects.filter(specialist = data)
  return render(request,'Specialtais/Specialtais.html',{'rs':email,'special':data})

def sprcialCardUnRe(request,data):
  data = doctor.objects.filter(specialist = data)
  return render(request,'Specialtais/Specialtais.html',{'special':data,'mm':data})

#doctor Profile
def doctor_profile(request,em_rec):
    doctorw=doctor.objects.get(email_recption = em_rec)
    return render(request,'doctor profile/dr-profile.html',{'doctor':doctorw,'dd':em_rec})

def doctor_profile_RE(request,email,em_rec):
    data = pactientaccount.objects.filter(mobilenumber=email)
    if data :
      name = data[0].mobilenumber
    else:
      data = medicalproviders.objects.filter(mobilenumber=email)
      name = data[0].mobilenumber
    name = data[0].first_name + data[0].last_name
    phone = data[0].mobilenumber
    date = datetime.today()
    timming = time.hour
    data1 = Bookedsession(name=name , phone = phone ,email_recep = em_rec)
    if request.POST:
      data1.save()
    doctorw=doctor.objects.get(email_recption = em_rec)
    return render(request,'doctor profile/dr-profile.html',{'doctor':doctorw,'dd':em_rec,'rs':email})
  

#login for medical
def medlogin(request):
  if request.method=='POST':       
    email1=request.POST['email']
    password1=request.POST['password']
    conut=0
     
    medicalproviderss = medicalproviders.objects.all()
    for e in medicalproviderss:
      if e.email == email1 and e.password == password1:
          name = medicalproviders.objects.filter(email=email1)
          name = name[0].mobilenumber
          return render(request,'Home/Home.html',{'rs':name })
          
    for f in medicalproviderss: 
      if  f.password != password1:
         messages.error(request,'kindly check your email and password :(')
         break
      
        
    
  return render(request,'patientlogin/index.html' ) 

  
    

#login for patient
def login(request):
  if request.method=='POST':       
    email1=request.POST['email']
    password1=request.POST['password']
    pactientaccounts = pactientaccount.objects.all()
    for e in pactientaccounts:
      if e.email == email1 and e.password == password1:
          name = pactientaccount.objects.filter(email=email1)
          name = name[0].mobilenumber
          return render(request,'Home/Home.html',{'rs':name })
    for f in pactientaccounts: 
      if  f.password != password1:
         messages.error(request,'kindly check your email and password :(')
         break 
  return render(request,'patientlogin/index.html')

     
     #else:
         #return redirect(request,'patientlogin/index.html')



     
     
          # patiantdata = patientLogin.objects.all()
          
          # email= patiantdata.objects.values_list('email')
   #if pactientaccount.objects.filter(password=request.POST.get('password' ))== password1 and pactientaccount.objects.filter(email=request.POST.get('email' ))== email1 :
          # if email1==email1 and password1==password1 :
          #     return redirect('index.html')
          # else:
          #      messages.error(request,'error')
          #      return render(request,'patientlogin/index.html')
      #if pactientaccount.objects.filter(password=request.POST.get('password') ).exists()==password and pactientaccount.objects.filter(email=request.POST.get('email') ).exists()==email:  
      
      
        #   for e in pactientaccount:
  #   if e.email==email1 and e.password == password1:
  #    return render(request,'patientlogin/index.html')
  #  else:
  #    messages.info(request,'error')  
  # return render(request,'patientlogin/index.html') 