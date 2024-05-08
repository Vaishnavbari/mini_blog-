from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator


# Create your models here.
class registration(AbstractUser):
     username = models.CharField(unique=True, max_length=50, null=True, blank=True, validators=[MinLengthValidator(2)])
     password = models.CharField(max_length=200,null=True, blank=True)
     first_name=models.CharField(max_length=50,null=True, blank=True)
     last_name=models.CharField(max_length=50,null=True, blank=True)
     password=models.CharField(max_length=50,null=True, blank=True)
     role=models.CharField(max_length=50,null=True, blank=True)


class addblog(models.Model):
     user_id=models.ForeignKey(registration,on_delete=models.CASCADE,default=None)
     title=models.CharField(max_length=200,null=True, blank=True)
     name=models.CharField(max_length=200,null=True, blank=True)
     location=models.CharField(max_length=200,null=True, blank=True)
     meassage=models.CharField(max_length=10000,null=True, blank=True)
