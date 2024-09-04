from django.db import models
from setup.basemodel import TimeBaseModel
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex

# Create your models here.

class WebPage(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [GinIndex(fields=['search_vector'])]
