from django.db import models

# Create your models here.
class Task (models.Model):
    title = models.CharField(max_length = 250)
    description = models.TextField()
    done = models.BooleanField(default = 0)
    created_at = models.DateTimeField()

class Person (models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    name = models.CharField(max_length = 250)
    sex = models.CharField(choices = SEX_CHOICES, max_length = 1)
