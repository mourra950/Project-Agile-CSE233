from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    committeeId = models.ForeignKey("Committee", on_delete=models.CASCADE)
    roleId = models.ForeignKey("Role", on_delete=models.CASCADE)


class Role(models.Model):
    name = models.CharField(max_length=20)
    urlId = models.ManyToManyField("Urls")
    # def __str__(self):
    #     return f"{self.id}: {self.name}"

class Urls(models.Model):
    name= models.CharField(max_length=20,unique=True)
    def __str__(self):
        return f"{self.id}: {self.name}"

class Committee(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    photo = models.CharField(max_length=30)
    headId = models.ForeignKey("User", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.id}: {self.name}"
   
class Tracker(models.Model):
    pass
