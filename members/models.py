from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
def arabic_slugify(str):
    # Add your custom logic here to convert Arabic characters to English characters
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace(" (", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    return str

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
    website = models.URLField(max_length=200)
    address = models.CharField(max_length=300)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(CoCategory)
    slug = models.SlugField(max_length=150, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.slug:
            self.slug = arabic_slugify(self.name)
        super(Company, self).save(*args, **kwargs)