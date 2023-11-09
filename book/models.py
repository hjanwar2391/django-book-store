from django.db import models

# Create your models here.

class BookModels(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description =  models.TextField()
    author = models.CharField(max_length=50)