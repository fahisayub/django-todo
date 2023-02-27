from django.db import models

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=200)
    isComplete=models.BooleanField(default=False)

    def __str_(self):
        return self.title