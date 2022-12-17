from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass

class Role(models.Model):
    pass

class Committee_des(models.Model):
    #Name=models.CharField(max_length=50)
    Description=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.id}: {self.Description}"
class Tracker(models.Model):
    pass
