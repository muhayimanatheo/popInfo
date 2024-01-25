from django.db import models

# Create your models here.
class Information(models.Model):
    fullname = models.CharField(max_length=200)
    birthdate = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    age = models.IntegerField(default=None)
    gender = models.CharField(max_length=200)
    provence = models.CharField(max_length=200)
    familymembers = models.IntegerField(default=None)
    resident = models.CharField(max_length=200)
    bankaccount = models.IntegerField(null=False)
    