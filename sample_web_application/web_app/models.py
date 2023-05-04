from django.db import models

# Create your models here.
class Review(models.Model):
    food_name = models.CharField(max_length=50)
    review = models.TextField()

    def __str__(self):
        return self.food_name