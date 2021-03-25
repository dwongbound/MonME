# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    image_url = models.CharField(max_length=40)
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    

class 
