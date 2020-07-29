from django.shortcuts import redirect,render,get_list_or_404,get_object_or_404,reverse,Http404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Doctor,Patient,Appointment
from .form import *
from doc_patient.form import CreateUserForm
from .filters import OrderFilter
from django.contrib.auth import login,logout,authenticate,SESSION_KEY,signals,tokens,user_logged_in,user_logged_out,_get_user_session_key
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required,PermissionDenied
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView,CreateView,DetailView,DeleteView,UpdateView
from django.contrib.auth.models import Group,Permission,User
from django.core.exceptions import ObjectDoesNotExist,PermissionDenied,RequestAborted,RequestDataTooBig,ValidationError,SuspiciousOperation
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.utils import cache,crypto,dates,duration,timezone
import random,string,Crypto
from django.middleware import cache,security,http
from django.dispatch import receiver
from django.test import selenium,testcases,client
from django.core.signals import request_finished,request_started
from django.db.models.signals import pre_save,post_delete,post_save

#no neeed to specify anything
@receiver([request_finished])
def my_callback(*args, **kwargs):
        print("Request finished !")
@receiver(post_save,sender=Appointment)        
def delnotifyer(sender,**kwargs):
        print("New Appointment has filled recently ")
@receiver(post_save,sender=Prescription)
@receiver(post_save, sender=Notification)        
def notifyer(sender,**kwargs):
        print("You have New Notifications")                   
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('doc_patient:home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
            #all first time user will be added to Patients group   
                user=form.save()
                username = form.cleaned_data.get('username')
                
            #Added username after video because of error returning customer name if not added
                messages.success(request, 'Account was created for ' + username)
                # my_group = Group.objects.get(name='my_group_name') 
                # my_group.user_set.add(your_user)
                return redirect('doc_patient:login')			
        context = {'form':form}
        return render(request, 'doc_patient/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('doc_patient:profile')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('doc_patient:profile')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'doc_patient/login.html', context)
          
def multistep(request):
        return render(request, 'doc_patient/multistep.html', {})
def logoutUser(request):
    logout(request)
    return redirect('doc_patient:login')
  
def appointment(request):
    # post=FormName(request.POST,request.FILES or None)
    # if post.is_valid():
            
        #    request.user.appointment=post.save()
        #    messages.success(request,"form filled")
        #    return  HttpResponseRedirect(reverse('doc_patient:home', ))
            
    return render(request, 'home.html',{})
@login_required(login_url='doc_patient:login')
def appointment_2(request):
    
    try:
        pass
    except :
        pass
    if request.user.appointment_set.all().exists():
        obj=True
    post=FormName(request.POST,request.FILES or None)
    if post.is_valid():
        #'name','age' ,'sex','mob','emailid','description','xray_1','video'
           p=Appointment()
           p.user=request.user
           p.name=request.POST.get('name')
           p.mob=request.POST.get('mob')
           p.age=request.POST.get('age')
           p.sex=request.POST.get('sex')           
           p.emailid=request.POST.get('emailid')
           p.description=request.POST.get('description')
           p.status=request.POST.get('status')
           p.doctorname=Doctor.objects.filter(id=request.POST.get('doctorname'))[0] 
           p.xray_1=request.FILES.get('xray_1')
           p.video=request.FILES.get('video')
           p.other=request.FILES.get('other')
           p.date= request.POST.get('date')          
           p.save()
           return  HttpResponseRedirect(reverse('doc_patient:home', ))
            
    return render(request, 'doc_patient/appointment.html',{'form':post})
 #all patient related work       
@login_required(login_url='doc_patient:login') 
def PatientsListView(request):
    try:
        pass
    except :
        pass
    else:
        pass
    object = request.user.doctor
    form = DoctorProfileForm(request.POST,request.FILES or None, instance=object)
    if form.is_valid():
        form.save() 
    mypatients = request.user.doctor.appointment_set.all()    
    myFilter = OrderFilter(request.GET, queryset=mypatients) 
    context = {'mypatients':mypatients, 
    'myfilter':myFilter,'form': form,'object':object}
    return render(request, 'doc_patient/patients.html',context)
 
def PatientDetailView(request,id):
    try:
        pass
    except :#expression as identifier
        pass
    obj=get_object_or_404(Appointment,id=id)
    post=PrescriptionForm(request.POST,request.FILES or None)
    if post.is_valid():
        newobj=Prescription()
        newobj.appointment=obj
        newobj.message=request.POST.get('message')
        newobj.test_result=request.POST.get('test_result')
        newobj.save()
        # self.prescription.message=
        # self.save()
            
    template_name='doc_patient/patient_detail.html' 
    return render(request, template_name, {'object':obj,'form':post,})

def PatientNotification(request,id):
    try:
        pass
    except :#expression as identifier
        pass
    obj=get_object_or_404(Appointment,id=id)
    notifyform=NotificationForm(request.POST,request.FILES or None)
    if notifyform.is_valid():
        notifyobj=Notification()
        notifyobj.appointment=obj
        notifyobj.notification=request.POST.get('notification')
        notifyobj.video_url=request.POST.get('video_url')
        notifyobj.save()
        # self.prescription.message=
        # self.save()
            
    template_name='doc_patient/patient_notification.html' 
    return render(request, template_name, {'object':obj,'notifyform':notifyform})


#all user profiles
@login_required(login_url='doc_patient:login')
def ProfileDetailView(request):
    #function need to be updateed ,not working on query not found
    try:
        object = request.user.appointment_set.all()
        
    except Appointment.DoesNotExist:
        return HttpResponse("<h1>First fill your form</h1>")
    return render(request, 'doc_patient/profile.html', {'obj':object})

def ProfilePrescription(request):
    #function need to be updateed ,not working on query not found
    try:
        object = request.user.appointment_set.all()
    except Appointment.DoesNotExist:
        return HttpResponse("<h1>First fill your form<h1>")
    return render(request, 'doc_patient/prescription.html', {'object':object})   



     
def ProfileNotification(request):
    #function need to be updateed ,not working on query not found
    try:
        object = request.user.appointment_set.all()
    except Appointment.DoesNotExist:
        return HttpResponse("<h1>First fill your form<h1>")
    return render(request, 'doc_patient/notification.html', {'object':object})      

    
class ProfileUpdateView(UpdateView):
    #user login required here  
    try:
        pass
    except :#expression as identifier
        pass
    template_name = 'doc_patient/profile_update.html'
    form_class = FormName

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Appointment, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('doc_patient:profile')
class ProfileDeleteView(DeleteView):
    try:
        pass
    except :#expression as identifier
        pass
    template_name = 'doc_patient/profile_delete.html'    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Patient, id=id_)

    def get_success_url(self):
        return reverse('doc_patient:home')

def doctor_detail_view(request):
    try:
        pass
    except :#expression as identifier
        pass
    obj = request.user.doctor
    context = {
        "object": obj
    }
    return render(request, "doc_patient/doctor_detail.html", context)

def doctor_update_view(request, id=id):
    try:
        pass
    except :#expression as identifier
        pass
    obj = get_object_or_404(Doctor, id=id)
    form=DoctorProfileForm(instance=obj)

    if request.method == 'POST':
        form = DoctorProfileForm(request.POST, request.FILES,instance=obj)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, "doc_patient/doctor_update.html", context)

def doctor_delete_view(request, id):
    try:
        pass
    except :#expression as identifier
        pass
    obj = get_object_or_404(Doctor, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "doc_patient/doctor_delete.html", context)   
# form = NewEventForm(request.POST or None)
#     if form.is_valid():
#         save_it = form.save(commit=False)
#         save_it.user = request.user
#         save_it.save()    
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
# import django.dispatch

# pizza_done = django.dispatch.Signal(providing_args=["toppings", "size"])         
#overriding clas based view and add this method to override
# def get_context_data(self, **kwargs):
#         # Call the base implementation first to get the context
#         context = super(BookListView, self).get_context_data(**kwargs)
#         # Create any data and add it to the context
#         context['some_data'] = 'This is just some data'
#         return context
    
  #admin or doctor login required here  method valid save
    # queryset=  Appointment.objects.filter(doctorname=name,treated_or_not=False)
    #also pass total number,total treated,etc
    #queryset=Appointment.objects.all()
    #template_name='doc_patient/patients.html'
    # def showpatient(request,id):
    #   x=(get_object_or_404(Appointment,id=id)).__dict__
    #   context={'obj':x,'len':len(x)}
    #   return render(request,  context)
       
    #from django.contri
# use just object to save something in model database  method is for saving appointment data

# def createpost(request):
#         if request.method == 'POST':
#             if request.POST.get('name') and request.POST.get('mob'):
#                 post=FormName()
                
#                 post.save()
                
#                 return render(request, 'home.html')  

#         else:
#                 return render(request,'home.html')

        
             
    
