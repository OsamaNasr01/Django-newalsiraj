from django.db import models
from django.utils.text import slugify

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(unique=True, auto_created=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name  
    
    