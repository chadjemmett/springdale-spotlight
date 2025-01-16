from django.db import models

# Create your models here.

class Color(models.Model):
    name = models.Charfield("Color Name", max_length=256)
    clicked = models.IntegerField()
    chosen = models.IntegerField()
    percent = models.FloatField(blank=True)
