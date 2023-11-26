from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Pet(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=30)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    guardian = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    created_on = models.DateTimeField(default=now)
