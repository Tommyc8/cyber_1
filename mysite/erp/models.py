from django.db import models
class User(models.model):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_lenght=30)

# Create your models here.
