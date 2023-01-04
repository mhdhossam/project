from datetime import datetime as zz
import datetime
from django.shortcuts import render
from .models import news
# Create your views here.

def check(d , dd ):
    now = zz.today()
    for s in range(1,32):
        lastd = now - datetime.timedelta(days = s)
        ddd = list (set(news.objects.filter(timing=lastd)))
        if ddd : break
    if d :
        data = d
    elif dd:
        data = dd
    elif ddd :
        data = ddd
    return data

def new(request):

    now = zz.today()
    d = list(
       set(news.objects.filter(timing=now))
    )
    lastd = now - datetime.timedelta(days = 1)
    dd = list (set(news.objects.filter(timing=lastd)))
    
    data = check(d,dd ).pop()
    data2 = check(d,dd).pop()
    data3 = check(d,dd).pop()
    data4 = check(d,dd).pop()
    data5 = check(d,dd).pop()
    data6 = check(d,dd).pop()
    data7 = check(d,dd).pop()
    data8 = check(d,dd).pop()
    data9 = check(d,dd).pop()
    data10 = check(d,dd).pop()

    return render(request,'news/index.html',{'new':data,
                                                   'new2':data2,'new3':data3,'new4':data4,'new5':data5,
                                                   'new6':data6,'new7':data7,'new8':data8,'new9':data9,
                                                   'new10':data10,'last':lastd})
def detail(request,title):
    detailing = news.objects.get(title = title)
    newss = news.objects.all()
    return render(request,'news/iindex.html',{'newss':detailing,'new':newss})


# news registered
def newRE(request,email):
    now = zz.today()
    d = list(
       set(news.objects.filter(timing=now))
    )
    lastd = now - datetime.timedelta(days = 1)
    dd = list (set(news.objects.filter(timing=lastd)))
    
    data = check(d,dd ).pop()
    data2 = check(d,dd).pop()
    data3 = check(d,dd).pop()
    data4 = check(d,dd).pop()
    data5 = check(d,dd).pop()
    data6 = check(d,dd).pop()
    data7 = check(d,dd).pop()
    data8 = check(d,dd).pop()
    data9 = check(d,dd).pop()
    data10 = check(d,dd).pop()
    return render(request,'news/index.html',{'new':data,
                                                   'new2':data2,'new3':data3,'new4':data4,'new5':data5,
                                                   'new6':data6,'new7':data7,'new8':data8,'new9':data9,
                                                   'new10':data10,'rs':email})


def detailRE(request,email,title):
    detailing = news.objects.get(title = title)
    newss = news.objects.all()
    return render(request,'news/iindex.html',{'newss':detailing,'rs':email,'new':newss})






