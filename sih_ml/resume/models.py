from django.db import models

# Create your models here.
class Result(models.Model):
    Resume=models.FileField(upload_to="files/")
    username=models.CharField(max_length=200)


class Text(models.Model):
    Txt=models.TextField()