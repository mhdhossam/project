# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
from django.shortcuts import render
from cmath import nan
from django.shortcuts import render
import pickle as pi
from medicalproviders.models import medicalproviders

from patientregister.models import pactientaccount

def consultUN(request):
    return render(request,'model-ai/index.html')

def consult(request , email):
    data = pactientaccount.objects.filter(mobilenumber=email)
    if data :
        name = data[0].mobilenumber
    else:
        data = medicalproviders.objects.filter(mobilenumber=email)
        name = data[0].mobilenumber
    return render(request,'model-ai/index.html',{'rs':name})

def check(results):
        if results == 1 :
            results1 = ' you are sick '
        elif results == 0 :
            results1 = 'you are not sick '
        else:
            results1 = 'insert you results'
        return results1

def Scaling(xx):
    from sklearn.impute import SimpleImputer
    fill_values = SimpleImputer(missing_values=np.nan, strategy="mean")
    xx = fill_values.fit_transform(xx)
    return xx

def inputDiabetes(request):
    if request.method=='POST': 
        age2 = request.POST.get('age2')
        Pregnancies = request.POST.get('Pregnancies')
        Glucose = request.POST.get('Glucose')
        BloodPressur = request.POST.get('BloodPressur')
        SkinThickness = request.POST.get('SkinThickness')
        Insulin = request.POST.get('Insulin')
        BMI = request.POST.get('BMI')
        DPFunction = request.POST.get('DPFunction')
        data = [Pregnancies,Glucose,
                BloodPressur,SkinThickness,
                Insulin,BMI,DPFunction,age2] 
        return data
    else:
        return None
    
def inputHeart(request):
    if request.method=='POST': 
        ag1 = request.POST.get('ag1')
        gender = request.POST.get('gender')
        impluse = request.POST.get('impluse')
        pressureHigh = request.POST.get('pressureHigh')
        pressureLow = request.POST.get('pressureLow')
        Glucose1 = request.POST.get('Glucose1')
        Kcm = request.POST.get('Kcm')
        troponin = request.POST.get('troponin')
        data = [ag1,gender,impluse,pressureHigh,
                pressureLow,Glucose1,Kcm,
                troponin] 
        return data
    else:
        return None


def ai(request,email):
    data = pactientaccount.objects.filter(mobilenumber=email)
    if data :
        name = data[0].mobilenumber
    else:
        data = medicalproviders.objects.filter(mobilenumber=email)
        name = data[0].mobilenumber
    if inputDiabetes(request) != None:
        values = [inputDiabetes(request)]
        ScalingValues = Scaling(values)
        # read trained model
        loaded_model = pi.load(open('ai/modelDiabetes3.sav','rb'))
        results = loaded_model.predict(ScalingValues)
    else:
        results  = ''
    return render(request,'model-ai/diabetes.html',{'rs':name,'rs2':check(results)})

def aiUnRE(request):
    if inputDiabetes(request) != None:
        values = [inputDiabetes(request)]
        ScalingValues = Scaling(values)
        loaded_model1 = pi.load(open('ai/modelDiabetes3.sav','rb'))
        results = loaded_model1.predict(ScalingValues)
    else:
        results  = ''
    return render(request,'model-ai/diabetes.html',{'rs2':check(results)})

def aiHER(request,email):
    data = pactientaccount.objects.filter(mobilenumber=email)
    if data :
        name = data[0].mobilenumber
    else:
        data = medicalproviders.objects.filter(mobilenumber=email)
        name = data[0].mobilenumber
    if inputHeart(request) != None:
        values = [inputHeart(request)]
        ScalingValues = Scaling(values)
        # read trained model
        loaded_model = pi.load(open('ai/modelHeart1.sav','rb'))
        results = loaded_model.predict(ScalingValues)
    else:
        results = ''

    return render(request,'model-ai/Heart.html',{'rs':name,'r3':check(results)})

def aiUnREHer(request):

    if inputHeart(request) != None:
        values = [inputHeart(request)]
        ScalingValues = Scaling(values)
        # read trained model
        loaded_model = pi.load(open('ai/modelHeart1.sav','rb'))
        results = loaded_model.predict(ScalingValues)
    else:
        results = ''

    return render(request,'model-ai/Heart.html',{'r3':check(results)})