# Generated by Django 3.0.4 on 2020-05-17 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_patient', '0009_auto_20200517_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='other',
            field=models.FileField(upload_to='files'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='xray_1',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
