from random import choice
from django.db import models
from django.db.models.deletion import CASCADE
from django_mysql.models import EnumField
from login.models import *
# Create your models here.
class syllabusfeed(models.Model):
    unit_no=EnumField(choices=['1','2','3','4','5'])
    title=models.CharField(max_length=150)
    subcode=models.ForeignKey('subjects',models.DO_NOTHING,blank=True,null=True,db_column='subcode')
    key=models.CharField(max_length=500)
    class Meta:
        db_table = 'syllabusfeed'
        managed = True
        models.UniqueConstraint(fields=['subcode', 'unit_no'], name="id")

class subjects(models.Model):
    subcode=models.CharField(max_length=9,primary_key=True)
    subject=models.CharField(max_length=70)
    dept=EnumField(choices=['CSE','IT','BT','ECE','EEE','MECH','AERO','CHEM'])
    sem=models.CharField(max_length=1)
    class Meta:
        db_table = 'subjects'
        managed = True

class enrolledsub(models.Model):
    uid=models.CharField(max_length=10)
    sub1=models.CharField(max_length=12)
    sub2=models.CharField(max_length=12)
    sub3=models.CharField(max_length=12)
    sub4=models.CharField(max_length=12)
    sub5=models.CharField(max_length=12)
    sub6=models.CharField(max_length=12)
    class Meta:
        db_table='enrolledsub'
        managed= True