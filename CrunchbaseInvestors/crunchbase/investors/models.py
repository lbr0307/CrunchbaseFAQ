from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


class Investor(models.Model):
    name = models.CharField(max_length = 100)
    institution = models.TextField()
    #notes = models.TextField()
    #tastes = models.TextField()
    #category = models.ForeignKey(Category, related_name='ingredients')

    def __str__(self):
        return self.name
