from django.db import models

# Create your models here.

class Employee(models.Model):
   
    name=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    office=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)
    status=models.BooleanField()

class Designation(models.Model):
    name=models.CharField(max_length=200)
    scale=models.IntegerField()
    ono=models.BooleanField(null=True)


class Emptren(models.Model):
   
    oo=models.CharField(max_length=200,)
    no=models.CharField(max_length=200)
    ddate=models.DateField(auto_created=True)

class EPD(models.Model):
   
    cnic=models.IntegerField(max_length=200,null=True)
    domicle=models.CharField(null=True,max_length=200)
    district=models.CharField(null=True,max_length=200)
    doj=models.DateField(null=True)
    DoB=models.DateTimeField(null=True)

 