# Generated by Django 3.0.4 on 2020-05-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_patient', '0004_auto_20200516_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='media/videos'),
        ),
    ]
