from django.db import models

class Film(model.Models):
    title = models.CharField(max_length=255)
    year = models.IntegerField(max_length=255)

    def __str__(self):
        return self.name

class Viewer(model.Models):
    name = models.CharField(max_length=255)
    age = models.IntegerField(max_length=255)
    films = models.ManyToManyField(Film)

    def __str__(self):
        return self.name
