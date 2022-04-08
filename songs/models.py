from random import choices
from turtle import title
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=255)
   

    def __str__(self):
        return str(self.title)

