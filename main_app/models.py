from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    book_name = models.CharField(max_length=100)
    price = models.IntegerField()
    author = models.CharField(max_length=100)
    