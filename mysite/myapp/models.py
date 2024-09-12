from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publish_date = models.DateField()

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

class Genre(models.Model):
    name = models.CharField(max_length=50)
