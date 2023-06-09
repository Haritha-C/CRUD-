from django.db import models

# Create your models here.
class Task(models.Model):
    slno = models.IntegerField()
    name = models.CharField(max_length=250)
    desc = models.TextField()

    def __str__(self):
        return self.name