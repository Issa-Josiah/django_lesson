from django.db import models

# Create your models here.
class Fist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    age=models.IntegerField(null=True, blank=True) 

    def __str__(self):
        return f"{self.name} - {self.age}"

