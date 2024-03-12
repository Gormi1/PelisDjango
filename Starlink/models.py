from statistics import mode
from turtle import title
from django.db import models

# Create your models here.

class Peliculas(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f"|----|{self.title} - {self.year}|----|"

