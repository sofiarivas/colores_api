from django.db import models


class Color(models.Model):
    name = models.CharField(blank=False, max_length=40)
    hexadecimal = models.CharField(unique=True, max_length=40)
    red = models.PositiveSmallIntegerField()
    green = models.PositiveSmallIntegerField()
    blue = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
