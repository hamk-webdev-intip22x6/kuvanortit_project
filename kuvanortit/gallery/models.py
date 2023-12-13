from django.db import models
from django.contrib.auth.models import User


class PictureFolder(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    mod_date = models.DateTimeField("date modified", auto_now=True)

    def __str__(self):
        return self.title


class Picture(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    tags = models.CharField(max_length=250)
    folder = models.ForeignKey(PictureFolder, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    mod_date = models.DateTimeField("date modified", auto_now=True)
    private = models.BooleanField()

    def __str__(self):
        return self.title
