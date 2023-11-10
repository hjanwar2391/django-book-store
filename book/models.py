from django.db import models

# Create your models here.

class BookModels(models.Model):
    Category ={
        ('category', 'category'),
        ('mistry','mistry'),
        ('ci fi','ci fi'),
        ('humar','humar'),
        ('Hurrur', 'hurrur')
    }
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description =  models.TextField()
    author = models.CharField(max_length=50)
    Category = models.CharField(max_length=30, choices=Category, default='hurrur')
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub = models.DateTimeField(auto_now=True)