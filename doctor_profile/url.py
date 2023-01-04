
from django.urls import re_path , path

from . import views
app_name='doctor_profile'
urlpatterns = [
    path('profile/<str:email>/<str:email_res>',views.profile,name='profile'),
]