# Generated by Django 3.0.4 on 2020-06-05 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_patient', '0029_auto_20200605_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='patient_id',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
