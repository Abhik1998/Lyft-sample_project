from django.contrib import admin
from doc_patient.models import *
# Register your models here.
class Urladmin(admin.ModelAdmin):
    list_display = ('appointment','video_call_url'   )

# Register the admin class with the associated model
admin.site.register(Url, Urladmin)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name','age' ,'sex',  )

# Register the admin class with the associated model
admin.site.register(Patient, PatientAdmin)
class PresAdmin(admin.ModelAdmin):
    list_display = ('appointment','message'   )

# Register the admin class with the associated model
admin.site.register(Prescription, PresAdmin)
class NotAdmin(admin.ModelAdmin):
    list_display = ('appointment','notification' ,'video_url'  )
    search_fields=['appointment']
    list_filter=['appointment']
# Register the admin class with the associated model
admin.site.register(Notification, NotAdmin)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name','age' ,'dept', 'timing', 'user')

# Register the admin class with the associated model
admin.site.register(Doctor, DoctorAdmin)
class AppointmentAdmin(admin.ModelAdmin):
    # def get_name(self, obj):
    #     return obj.message
    list_filter=['age','doctorname','date_created','date']
    list_display = ('sex', 'doctorname','status','date','user','appointment_id')
    search_fields=['name']
    ordering=['name']
admin.site.register(Appointment, AppointmentAdmin)  
   # autocomplete_fields=['Choice']