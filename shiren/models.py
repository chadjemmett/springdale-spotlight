from django.db import models

# Create your models here.

class Price(models.Model):
    price = models.IntegerField()


class Item(models.Model):
    TYPE = [
            (10, 'Herb'),
            (20, 'Scroll'),
            (30, 'Bracelet'),
            (40, 'Jar'),
            (50, 'Staff'),
            ]
    
    item_name = models.CharField(max_length=256)
    item_type = models.IntegerField(choices=TYPE)
    found = models.BooleanField(default=False, blank=True)
    price = models.ManyToManyField(Price)

    def __str__(self):
        return f"{self.item_name}, {self.item_type}"
