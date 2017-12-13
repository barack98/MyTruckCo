from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    album_logo = models.CharField(max_length=250)

    def __str__(self):
        return self.album_title

class Picture(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    photos = models.CharField(max_length=250)
