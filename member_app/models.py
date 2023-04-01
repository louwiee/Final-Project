from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class MemberProfile(models.Model):
    MEM_NUM = models.IntegerField(primary_key=True, ) 
    MEM_FNAME = models.CharField(max_length=300, null=True)  
    MEM_LNAME = models.CharField(max_length=300, null=True) 
    MEM_STREET = models.CharField(max_length=300, null=True)
    MEM_CITY = models.CharField(max_length=300, null=True)
    MEM_STATE = models.CharField(max_length=300, null=True)
    MEM_ZIP = models.CharField(max_length=300, null=True)
    MEM_BALANCE = models.CharField(max_length=300, null=True)


def __str__(self):
    return str(self.user)
