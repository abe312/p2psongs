from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Album(models.Model):

    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    logo = models.CharField(max_length=2500)

    def __unicode__(self):
        return self.title + " - " + self.artist


class Song(models.Model):

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
