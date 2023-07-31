from django.db import models
from django.utils.text import slugify

# Create your models here.

def arabic_to_english_slug(text):
    # Define a dictionary that maps Arabic characters to their corresponding English characters
    arabic_to_english_map = {
        'ا': 'a',
        'أ': 'a',
        'إ': 'e',
        'ب': 'b',
        'ت': 't',
        'ث': 'th',
        'ج': 'j',
        'ح': 'h',
        'خ': 'kh',
        'د': 'd',
        'ذ': 'th',
        'ر': 'r',
        'ز': 'z',
        'س': 's',
        'ش': 'sh',
        'ص': 's',
        'ض': 'dh',
        'ط': 't',
        'ظ': 'dth',
        'ع': '3',
        'غ': 'gh',
        'ف': 'f',
        'ق': 'q',
        'ك': 'k',
        'ل': 'l',
        'م': 'm',
        'ن': 'n',
        'ه': 'h',
        'و': 'w',
        'ي': 'y',
        'ئ': 'e',
        'ء': 'a',
        'ؤ': 'o',
        'ة': 'h',
        'ى': 'a',
        # Add more mappings here
    }
    # Create a new string that replaces the Arabic characters with their corresponding English characters
    english_text = ''.join([arabic_to_english_map.get(char, char) for char in text])
    # Use the Django slugify function to generate the slug from the English text
    slug = slugify(english_text)
    return slug

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    parent_id = models.PositiveIntegerField(null=True)
    slug = models.SlugField(max_length=150, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.slug:
            self.slug = arabic_to_english_slug(self.name)
        super(Category, self).save(*args, **kwargs)


class Brand(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=25)
    description = models.TextField(max_length=500)
    category = models.ManyToManyField(Category, related_name='brands')
    slug = models.SlugField(max_length=150, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.slug:
            self.slug = arabic_to_english_slug(self.name)
        super(Brand, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=150, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.slug:
            self.slug = arabic_to_english_slug(self.name)
        super(Product, self).save(*args, **kwargs)



class Price(models.Model):
    value = models.FloatField()
    product = models.ForeignKey(Product, related_name='prices', on_delete=models.CASCADE)



class Spec(models.Model):
    name = models.CharField(max_length=50)
    type = models.IntegerField(choices=[
        (1, 'Numeric'),
        (2, 'Text'),
        (3, 'Boolean'),
    ])
    unit = models.CharField(max_length=50, null=True)
    category = models.ForeignKey(Category, related_name='specs', on_delete=models.CASCADE)

class NumericSpec(models.Model):
    value = models.FloatField()
    spec = models.ForeignKey(Spec, related_name='numeric', on_delete=models.CASCADE)



class TextSpec(models.Model):
    value = models.FloatField()
    spec = models.ForeignKey(Spec, related_name='text', on_delete=models.CASCADE)



class BooleanSpec(models.Model):
    value = models.FloatField()
    spec = models.ForeignKey(Spec, related_name='bool', on_delete=models.CASCADE)