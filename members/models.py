from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CoCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    wesite = models.URLField(max_length=200)
    address = models.CharField(max_length=300)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(CoCategory)
    slug = models.SlugField(unique=True, auto_created=True)

    def __str__(self):
        return self.name