from django.urls import path,include


from . import views
app_name='logincards'
urlpatterns = [
    path('sigin',views.sigin,name='sigin'),
]
