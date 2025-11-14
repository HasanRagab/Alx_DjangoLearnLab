from django.db import models
from django.apps import apps
from django.conf import settings

# Reference the actual custom user model so static tools can resolve it:
CustomUser = apps.get_model(settings.AUTH_USER_MODEL)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"