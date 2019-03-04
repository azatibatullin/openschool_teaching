from django.db import models

# Create your models here.
class Discipline(models.Model):
    name = models.TextField()
    description = models.TextField()