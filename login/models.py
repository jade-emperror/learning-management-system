from django.db import models
from django.db.models.enums import Choices
from django_mysql.models import EnumField
# Create your models here.

class Faculty(models.Model):
    uid=models.CharField(max_length=10,null=False,blank=False,primary_key=True)
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=20,null=False,blank=False)
    gender=EnumField(choices=['M','F','non-binary','rather not say'],default="rather not say")
    phno=models.CharField(max_length=10,null=False,blank=False)
    email=models.CharField(max_length=30,null=False,blank=False)
    class Meta:
        managed = True
        db_table = 'faculty'
        
class Student(models.Model):
    uid=models.CharField(max_length=10,null=False,blank=False,primary_key=True)
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=20,null=False,blank=False)
    gender=EnumField(choices=['M','F','non-binary','rather not say'],default="rather not say")
    phno=models.CharField(max_length=10,null=False,blank=False)
    email=models.CharField(max_length=30,null=False,blank=False)
    dept=EnumField(choices=['IT','BT','CSE','ECE','EEE','MECH','CIVIL'])
    semester=models.IntegerField(default=1)
    class Meta:
        managed = True
        db_table = 'student'