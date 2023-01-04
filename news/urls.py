from django.contrib import admin
from django.urls import include, path
from . import views
app_name = 'news'
urlpatterns = [
    path('news',views.new,name='news'),
    path('detail/<str:title>',views.detail,name='detail'),
    path('news/<str:email>',views.newRE,name='newsRE'),
    path('detail/<str:email>/<str:title>',views.detailRE,name='detailRE')
]