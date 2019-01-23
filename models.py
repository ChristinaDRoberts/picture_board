from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length = 255)
    picture = models.URLField()
    description = models.TextField()





