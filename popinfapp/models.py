from django.db import models

# Create your models here.
class Information(models.Model):
    fullname = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    age = models.IntegerField(default=None)
    gender = models.CharField(max_length=200)
    provence = models.CharField(max_length=200)
    familymembers = models.IntegerField(default=None)
    