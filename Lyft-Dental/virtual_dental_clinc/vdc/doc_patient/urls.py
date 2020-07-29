from django.urls import path, re_path
from django.shortcuts import HttpResponse,render,reverse,HttpResponseRedirect,redirect
from .views import appointment,PatientsListView,PatientDetailView,appointment_2
from  .views import   ProfileDetailView ,ProfileUpdateView,ProfileDeleteView,ProfilePrescription,ProfileNotification
from django.conf import settings
from .models import Patient
from django.contrib.auth.decorators import login_required
from doc_patient import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
app_name = 'doc_patient'
def chat(request,name,id):
    return render(request, 'doc_patient/index.html', {})
def treated(request,**args):
    return HttpResponse("<h1>Patient marked as treated<h1>")
# def video_call(request):
#      return redirect()   
# passing using slug field in custom method 
urlpatterns = [
    #path('https://appr.tc/r/<slug:id>', name='doctor_detail'),
    path('',appointment,name='home'),
    path('register/', views.registerPage, name="register"),
    path('multistep/', views.multistep, name="multistep"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('appointment/',appointment_2,name='appointment_2'),
    path('patients/<int:id>/',views.PatientDetailView, name='patient_detail'),    
    path('notification/<int:id>/',views.PatientNotification,name='patient_notification'), 
    path('chat/<str:name>/<int:id>/',chat,name='chat'),    
    path('profile/',(ProfileDetailView),name='profile'),
    path('profile/prescription/',(ProfilePrescription),name='prescription'),
    path('profile/notification/',(ProfileNotification),name='notification'),
    path('patients/',views.PatientsListView,name='patients'),
    path('patients/<int:id>/<var>/',treated, name='treated_or_not'),
    path('doctor/',views.doctor_detail_view, name='doctor_detail'), 
    path('doctor/<int:id>/update/',views.doctor_update_view, name='doctor_update'),  
    path('doctor/<int:id>/delete/', views.doctor_delete_view, name='doctor_delete'),
    path('profile/<int:id>/update/',login_required (ProfileUpdateView.as_view()), name='profile_update'),
    path('profile/<int:id>/delete/', login_required(ProfileDeleteView.as_view()), name='profile_delete'),
# 
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)+staticfiles_urlpatterns()
