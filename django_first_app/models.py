from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    page_count = models.IntegerField()
    rating = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

