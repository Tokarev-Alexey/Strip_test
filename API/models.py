from django.db import models


class Item(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
