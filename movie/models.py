from django.db import models

# Create your models here.

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.title
