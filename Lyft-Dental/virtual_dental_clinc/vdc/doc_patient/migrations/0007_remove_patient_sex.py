# Generated by Django 3.0.4 on 2020-05-16 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doc_patient', '0006_auto_20200516_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='sex',
        ),
    ]
