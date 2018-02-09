from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50, unique=True)
    score = models.IntegerField() #maybe create a review class
    review = models.TextField()

    def __str__(self):
        return self.name
