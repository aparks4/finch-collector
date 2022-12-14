from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Finch(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta: 
        ordering = ["name"]

class Picture(models.Model):
    title = models.CharField(max_length=150)
    url = models.CharField(max_length=250)
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE, related_name="pictures")

    def __str__(self):
        return(self.title)

class Album(models.Model):

    title = models.CharField(max_length=150)
    pictures = models.ManyToManyField(Picture)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title