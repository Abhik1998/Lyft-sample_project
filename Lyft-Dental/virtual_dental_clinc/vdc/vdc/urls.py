"""vdc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render,redirect
from django.http import request
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
app_name = 'project'
def home(request):
     return render(request, 'home.html', {}) 
def login(request):
     return render(request, 'login.html', {})       
def signup(request):
     return render(request, 'signup.html', {}) 
def shop(request):
     return render(request, 'widget.html', {}) 
def patients(request):
     return render(request, 'patients.html', {})  
def payment(request):
     return render(request,'payment.html',{})
# def payment(request):
#      return redirect('http://127.0.0.1:8085/payment/user/')                   
urlpatterns = [
    path('',include('doc_patient.urls')),
   # path(r'^accounts/login/$', include('django.contrib.auth.views.login'),
    #path('appointment/',),
    path('admin/', admin.site.urls),
    path('shop/',shop),
    path('payment/',payment,name='payment'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

