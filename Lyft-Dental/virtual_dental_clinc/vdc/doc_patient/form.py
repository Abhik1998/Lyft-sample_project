from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField


    #my_field = DateField(widget=AdminDateWidget)    
class FormName(forms.ModelForm):
    name       = forms.CharField(label='Name', 
                    widget=forms.TextInput(attrs={"placeholder": "Your Name","rows": 1,
                                    'cols': 2}))
    #date = models.DateField(auto_now=False, auto_now_add=False,)
    #date = forms.DateField(auto_now=False, auto_now_add=False)
    
    date = forms.DateField(widget=forms.TextInput(attrs={"placeholder": "formate 2020-12-15"}))
                                  
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 10,
                                    'cols': 30
                                }
                            )
                        )
    emailid       =  forms.EmailField(required=True,widget=forms.TextInput(attrs={"placeholder": "Your EmailId"}))
    class Meta:
        model = Appointment
        fields = ['name','age','sex','status','date','mob','emailid','description','doctorname','xray_1','video','other']
        #widgets = {'user': forms.HiddenInput()}
        #fields=['name','age',]
       #emailid and description is giving error or not getting into database or its not getting valid on form.isvalid
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']  
class  DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name','age','dept','timing','profile_pic']          
class PrescriptionForm(forms.ModelForm):
    message = forms.CharField(label='Prescription',
                        required=True, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "formate   Drug name | drug number | total days | dosage",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 10,
                                    'cols': 45
                                }
                            )
                        )
    class Meta:
        model= Prescription  
        #fields=all_fields
        fields =['hospital','doctor','patient','patient_id','age','sex','message','test_result','video',]    
class NotificationForm(forms.ModelForm):
    notification = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "type notification.example:Your meeting is scheduled at x time",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 10,
                                    'cols': 30
                                }
                            )
                        )
    class Meta:
        model= Notification         
        fields =['notification','video_url']
class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['video_call_url']