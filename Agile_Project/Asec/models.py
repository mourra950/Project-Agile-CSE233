from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    committeeId = models.ForeignKey("Committee", default=1,on_delete=models.CASCADE)
    roleId = models.ForeignKey("Role", default=1,on_delete=models.CASCADE)



class Role(models.Model):
    name = models.CharField(max_length=20)
    urlId = models.ManyToManyField("Urls")
    def __str__(self):
        return f"{self.name}"

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
        return f"{self.id}: Team {self.name}"
class announcements(models.Model): 
    name= models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    facebookLink=models.CharField(max_length=150)
    def __str__(self):
        return f"{self.name}: {self.description}"
class Tracker(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE,default='-1',related_name='attendance')
    task = models.CharField(max_length=255,default='No task yet')
    attendance = models.BooleanField(null=False,default=True)
    description = models.CharField(max_length=255,default='Without description')
