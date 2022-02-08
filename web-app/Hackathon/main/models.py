from django.db import models

# Create your models here.
class ideas(models.Model):
    idea = models.CharField(max_length=200)

    def __str__(self):
        return self.idea