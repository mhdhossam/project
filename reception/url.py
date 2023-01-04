from django.urls import re_path , path

from . import views
app_name='reception'
urlpatterns = [
    path('reception/<str:email>',views.reception,name='reception'),
]