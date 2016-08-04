from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class posts(models.Model):
    title_post = models.CharField(max_length=120)
    image = models.FileField(null=True,blank=True)
    info = models.TextField()
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField( auto_now= False,auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title_post



