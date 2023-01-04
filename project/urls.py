"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, url
    2. Add a URL to urlpatterns:  url('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('patientregister/',include('patientregister.url',namespace='patientregister')),
    path('medicalprovider/',include('medicalproviders.url',namespace='medicalproviders')),
    path('registas/',include('registeras.url',namespace='registeras')),
    path('',include('Home.url',namespace='Home')),
    path('sigin/',include('logincards.url',namespace='logincards')),
    path('',include('patientlogin.url',namespace='patientlogin')),
    path('',include('ai.url',namespace='ai')),
    path('',include('doctor.url',namespace='doctor')),
    path('',include('news.urls',namespace='news')),
    path('', include('doctor_profile.url', namespace='doctor_profile')),
    path('', include('reception.url', namespace='reception')),
    
    
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

