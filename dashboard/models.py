from random import choice
from django.db import models
from django.db.models.deletion import CASCADE
from django_mysql.models import EnumField

# Create your models here.
class syllabusfeed(models.Model):
    unit_no=EnumField(choices=['1','2','3','4','5'])
    subcode=models.ForeignKey('subjects',models.DO_NOTHING,blank=True,null=True,db_column='subcode')
    key=models.CharField(max_length=200)
    class Meta:
        db_table = 'syllabusfeed'
        managed = True
        models.UniqueConstraint(fields=['subcode', 'unit_no'], name="id")

class subjects(models.Model):
    subcode=models.CharField(max_length=9,primary_key=True)
    subject=models.CharField(max_length=50)
    dept=EnumField(choices=['CSE','IT','BT','ECE','EEE','MECH','AERO','CHEM'])
    sem=models.CharField(max_length=1)
    class Meta:
        db_table = 'subjects'
        managed = True

class enrolledsub(models.Model):
    uid=models.CharField(max_length=10,null=False,blank=False,primary_key=True)
    sub1=models.ForeignKey('subjects',models.DO_NOTHING,blank=True,null=True,db_column='subcode1',related_name='subcode1')
    sub2=models.ForeignKey('subjects',models.DO_NOTHING,blank=True,null=True,db_column='subcode2',related_name='subcode2')
    sub3=models.ForeignKey('subjects',models.DO_NOTHING,blank=True,null=True,db_column='subcode3',related_name='subcode3')
    sub4=models.ForeignKey('subjects',models.DO_NOTHING,blank=True,null=True,db_column='subcode4',related_name='subcode4')
    sub5=models.ForeignKey('subjects',models.DO_NOTHING,blank=True,null=True,db_column='subcode5',related_name='subcode5')
    sub6=models.ForeignKey('subjects',models.DO_NOTHING,blank=True,null=True,db_column='subcode6',related_name='subcode6')
    class Meta:
        db_table='enrolledsub'
        managed= True