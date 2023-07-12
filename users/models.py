from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.slug
    # add any other fields you see as important
