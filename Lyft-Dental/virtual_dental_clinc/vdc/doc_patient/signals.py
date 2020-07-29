from django.db.models import signals
from django.core.signals import got_request_exception,request_finished,request_started,setting_changed
from django.db.models.signals import pre_save,post_delete,post_save
from django.dispatch import receiver
from myapp.models import MyModel
@receiver(request_finished)
    def my_callback(sender, **kwargs):
        print("Request finished!")