from django.urls import path,include


from . import views
app_name='registeras'
urlpatterns = [
    path('register',views.register,name='register'),
]
