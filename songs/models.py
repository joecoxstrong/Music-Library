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
    liked = models.ManyToManyField(User, default=None, blank=True)

    def __str__(self):
        return str(self.title)

    @property
    def num_likes(self):
        return self.liked.all().count()    

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    value = models.CharField(choices, default='Like', max_length=10)

    def __str__(self):
        return str(self.song)