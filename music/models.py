from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.artist
        return self.album_title
        return self.genre
        return self.album_logo


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

    def __unicode__(self):
        return self.album
        return self.file_type
        return self.song_title
