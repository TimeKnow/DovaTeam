from django.db import models
from django.conf import settings
# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=120)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return str(self.name)
