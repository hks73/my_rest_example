from __future__ import unicode_literals

from django.db import models
from django import forms
# Create your models here.


class user(models.Model):
    user_name   =  models.CharField(max_length=200)
    user_date   =  models.DateTimeField('date published')
    user_email  =  models.CharField(max_length=200)
    user_stream =  models.CharField(max_length=200)
