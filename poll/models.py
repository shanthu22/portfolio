from django.db import models

class profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='useruploadedpics', height_field=300, width_field=300, max_length=300)
    description = models.TextField()
    email = models.EmailField(max_length=254)
class checking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='useruploadedpics', height_field=300, width_field=300, max_length=300)
    description = models.TextField()
    email = models.EmailField(max_length=254)
class certificates(models.Model):
    picture = models.TextField()
    description = models.TextField()
   
    