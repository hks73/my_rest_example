from __future__ import unicode_literals

from django.db import models
from django import forms
from django.forms import ModelForm
# Create your models here.


class user(models.Model):
    user_name      =  models.CharField(max_length=200)
    user_email     =  models.CharField(max_length=200)
    user_stream    =  models.CharField(max_length=200)

class userForm(ModelForm):
    class Meta:
        model = user
        fields = ['user_name', 'user_email','user_stream']
