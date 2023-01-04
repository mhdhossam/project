from django.urls import re_path , path

from . import views
app_name='patientlogin'
urlpatterns = [
    path('login',views.login,name='login'),
    path('homeuser/<str:email>',views.homeuser,name="home"),
    path('medlogin',views.medlogin,name='medlogin'),
    path('specialtais/<str:email>',views.cards,name='cards'),
    path('specialtais',views.cardsUnRe,name='cardsUnRe'),
    path('specialtaisaa/<str:data>',views.sprcialCardUnRe,name='sprcialCardUnRe'),
    path('specialtaisaa/<str:email>/<str:data>',views.sprcialCard,name='sprcialCard'),
    path('doctor/<str:em_rec>',views.doctor_profile,name='doctor'),
    path('doctor/<str:email>/<str:em_rec>',views.doctor_profile_RE,name='doctorRE'),
]