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
    class Meta:
        db_table = 'subjects'
        managed = True