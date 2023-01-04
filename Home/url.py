from django.urls import path,include


from . import views
app_name='Home'
urlpatterns = [
    path('home',views.Home,name='Home'),
]
