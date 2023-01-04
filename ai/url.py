from django.urls import path,include


from . import views
app_name='ai'
urlpatterns = [
    path('ai/<str:email>/diabetes',views.ai,name='aiDiabetes'),
    path('ai/<str:email>/heart',views.aiHER,name='aiHeart'),
    path('ai/diabetes',views.aiUnRE,name='aiUnReDiabetes'),
    path('ai/heart',views.aiUnREHer,name='aiUnReHeart'),
    path('consult',views.consultUN, name='consultUN' ),
    path('consult/<str:email>',views.consult, name='consult' ),
    
]
