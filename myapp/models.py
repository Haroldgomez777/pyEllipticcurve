from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from registration.models import *


class Document(models.Model):
    # uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    uploader = models.CharField(max_length=100)
    docfile = models.FileField(upload_to='documents')


class Msg(models.Model):
    
    user = models.CharField(max_length=100)
    encmsg = models.TextField()
    decmsg = models.TextField()
	
    def __str__(self):
            return '%s %s ' % (self.user)
