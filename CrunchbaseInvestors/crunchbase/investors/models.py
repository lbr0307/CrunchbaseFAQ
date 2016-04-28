from django.db import models

class People(models.Model):
    name = models.CharField(max_length = 100)
    birthPlace = models.TextField()
    affiliationName = models.TextField()

    def __str__(self):
        return self.name


class Investor(models.Model):
    name = models.CharField(max_length = 100)
    institution = models.TextField()
    people = models.ForeignKey(People, related_name = 'investors')

    def __str__(self):
        return self.name
