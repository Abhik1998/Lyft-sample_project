from django.db import models
from django.shortcuts import render,redirect,reverse,get_list_or_404,get_object_or_404
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.forms import Form
from django.contrib.auth.models import User
from django.urls import path,include,URLPattern
from datetime import date
import random
sex_types=( 
    ("male", "male"), 
    ("female", "female"), 
    ("Blank", "Blank"), )
  
# Create your models here. abstract class appointment.objects.total_appointment('today_date')

class Doctor(models.Model):
    profile_pic = models.ImageField(default="profile.jpeg", null=True, blank=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name=  models.CharField(max_length = 150,null=False)
    age = models.DecimalField(max_digits=2, decimal_places=0,blank=True, null=True)    
    dept= models.CharField(max_length = 150)
    timing = models.DateTimeField(auto_now=False, auto_now_add=False)
    #patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    def __str__(self):
         return self.name
    def get_absolute_url(self):
        return reverse("doc_patient:doctor_detail", kwargs={"id": self.id})
    def edit_profile(self):
        return reverse("doc_patient:doctor_update", kwargs={"id": self.id})        
    def profile_delete(self):
        return reverse("doc_patient:doctor_delete", kwargs={"id": self.id})        
     
    def chat(self,id):
        pass
    def call(self,id):
        pass 
    def notify(self,time,date):
        pass 
    def view_appointment(self):
        return Appointment.object.all(new_patient=True)
        #fetch all object that 
    def view_patient(self):
        return Patient.object.all(new_patient=True)
#should patient inherited or make foreign  in appointment
class Patient(models.Model): 
    name = models.CharField(max_length = 150)
    age = models.DecimalField(max_digits=100, decimal_places=0)
    sex = models.CharField(max_length = 100,choices=sex_types,default='male')
    mob = models.DecimalField(max_digits=10, decimal_places=0,)            
    emailid = models.EmailField(max_length=254)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("doc_patient:patient_detail", kwargs={"id": self.id})
    def edit_profile(self):
        return reverse("doc_patient:profile_update", kwargs={"id": self.id})        
    def profile_delete(self):
        return reverse("doc_patient:profile_delete", kwargs={"id": self.id})        
    def edit_appointment(self):
        pass 
    
    def call(self):
        pass 
    def video_call(self):
        pass 
    def notify(self,time,date):
        pass  
    def view_appointment(self):
        pass 
        #fetch all object that use  Appointment.object.all(new_patient=True)
    def payfee(self):
        pass
    def delete_appointment(self):
        pass
    
        
# Attributes(Columns)-Functions-Edit profile()edit appointment()payment()delete()
# Name,Age ,sex,Mob. Number,email id,unique ID(pk) 
import uuid
# class appointmentManager(models.Manager):
#     def total_appointment(self, date):
#         return self.filter(date_created='date_today').count()
#appointment id is not set as primary key
class Appointment (Patient):
    appointment_id = models.UUIDField( editable = False ,default=uuid.uuid4, help_text='Unique ID for this appointment',blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE,blank=True,)
    STATUS =(
        ('General','General'),
        ('Urgent','Urgent'),
        ('Regular Checkup','Regular Checkup')
    )
    profile_pic = models.ImageField(default="/media/profile.jpeg", null=True, blank=True,upload_to="images/")
    status=models.CharField(null=True,choices=STATUS, max_length=50,default='General')
    date = models.DateField(auto_now=False, auto_now_add=False,null=True,)
    treated_or_not=models.BooleanField(default=False,blank=True,editable=True)
    payment = models.BooleanField(default=False,blank=True)    
    doctorname = models.ForeignKey(Doctor, null=True, on_delete=models.CASCADE)    
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(null=True,max_length=500)
    video = models.FileField(upload_to='videos/',blank=True,null=True)
    xray_1 = models.ImageField(upload_to='images/',blank=True, null=True)
    other = models.FileField(upload_to='files/',blank=True,null=True)

    # objects = appointmentManager() to table level queries
    class Meta:
        ordering = ['date_created']
    def __unicode__(self):
        return self.name    
    def __str__(self):
        return self.name    
    def create(self):
        pass 
    def is_treated(self):   
        self.treated_or_not=True
        self.save()
    # def chat(self):
    #     return reverse("doc_patient:chat",kwargs={"id": self.id})   
    def get_video_call_url(self):
        y=(self.name)+str(date.today())
        return HttpResponseRedirect("https://appr.tc/r/123456")
        
        #return reverse("doc_patient:video_call", kwargs={"id": y})    
    # @property    
    # def create_url(self):
    #    x= ""
    #    y=str(random.randint(10000,10000000000) )
    #    obj = Url.objects.create(appointment=self,video_call_url=x+y)     
    #    return self.url.video_call_url
        
        
        #return reverse(request.path_info)reverse("doc_patient:treated_or_not",kwargs={"var": 4})
        
    def share_patient_to_doc(self,id):
        self.doctorname=Appointment.objects.get(id=id)
        self.save()
class Prescription(models.Model):
    hospital=models.CharField(max_length=150,default='Virtual Dental Clinic',null=True)
    doctor=models.CharField(max_length = 150,null=True)
    patient = models.CharField(max_length = 150,null=True)
    patient_id = models.CharField(max_length = 200,null=True)    
    date = models.DateTimeField(auto_now_add=True, null=True)
    age = models.DecimalField(max_digits=3, decimal_places=0,null=True)
    sex = models.CharField(max_length = 100,default='male')    
    appointment=models.ForeignKey(Appointment, on_delete=models.SET_NULL,null=True)
    message = models.TextField(null=True,max_length=500)
    test_result=models.FileField(upload_to='files/',blank=True,null=True)
    video=models.FileField(upload_to='videos/',blank=True, null=True)
   # time_stamp=models.DateTimeField( auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.message   
class Notification(models.Model):
    appointment=models.ForeignKey(Appointment, on_delete=models.SET_NULL,null=True)
    notification = models.TextField(null=True,max_length=500)
    video_url = models.URLField(max_length = 200,blank=True, null=True)
    
    #time_stamp=models.DateTimeField( auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.appointment.name 
        #no use of url table   
class Url(models.Model):
    appointment=   models.ForeignKey(Appointment,  on_delete=models.SET_NULL, null=True )
    video_call_url = models.URLField(max_length = 100,null=True)
    


    def __str__(self):
        return self.video_call_url
        
#form submission from deoctor and receiving from patient using button
# class MyModel(object):
#   @property
    # def value(self): 
    #     print('Getting value') 
    #     return self._value 
          
    # # setting the values     
    # @value.setter 
    # def value(self, value): 
    #     print('Setting value to ' + value) 
    #     self._value = value 
          
    # # deleting the values 
    # @value.deleter 
    # def value(self): 
    #     print('Deleting value') 
    #     del self._value 
# access it useing object.value(like an attribute)    

    
