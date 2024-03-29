# Generated by Django 3.0.4 on 2020-05-09 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.DecimalField(decimal_places=0, max_digits=100)),
                ('sex', models.CharField(choices=[('1', 'male'), ('2', 'female'), ('3', "don't wanna tell")], default='male', max_length=100)),
                ('mob', models.CharField(max_length=12)),
                ('emailid', models.EmailField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('patient_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='doc_patient.Patient')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('description', models.TextField()),
                ('xray_1', models.ImageField(upload_to=None)),
                ('xray_2', models.ImageField(upload_to=None)),
            ],
            bases=('doc_patient.patient',),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('dept', models.CharField(max_length=150)),
                ('timing', models.DateTimeField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc_patient.Patient')),
            ],
        ),
    ]
