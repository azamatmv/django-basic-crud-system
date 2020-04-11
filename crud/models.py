from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from mysite import settings



class Books(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.IntegerField()
    author = models.CharField(blank=False, max_length=200)
    def __unicode__(self):
        return self.name