from email.policy import default
from django.db import models
class data(models.Model):
    
    name=models.CharField(max_length=122,default="")
    snippet=models.CharField(max_length=500,default="")

# Create your models here.
