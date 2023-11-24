from django.db import models
from django.contrib.auth.models import User


class Pet(models.Model):
    name = models.CharField(max_length=30)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    guardian = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
