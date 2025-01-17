from django.db import models

# Create your models here.

class Color(models.Model):
    name = models.CharField("Color Name", max_length=256)
    clicked = models.IntegerField(default=1)
    chosen = models.IntegerField(default=1)
    percent = models.FloatField(blank=True, default=1)

    def __str__(self):
        return f"{self.name}, Clicked: {self.clicked}, Chosen: {self.chosen}, Percent: {self.percent} "
