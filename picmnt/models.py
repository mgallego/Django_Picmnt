from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=140)
    local = models.IntegerField(default=1)
