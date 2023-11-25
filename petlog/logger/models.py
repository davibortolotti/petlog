from django.db import models

from petlog.pets.models import Pet


class AbstractEntry(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        abstract = True


class Entry(AbstractEntry):
    pass


class Vaccine(AbstractEntry):
    vaccine_type = models.CharField(max_length=30)
    given_on = models.DateField()
    given_at = models.CharField(max_length=30)
    given_by = models.CharField(max_length=30)
    next_dose = models.DateField()


class Symptom(AbstractEntry):
    title = models.CharField(max_length=50)
    description = models.TextField()


class Training(AbstractEntry):
    pass


class Medicine(AbstractEntry):
    name = models.CharField(max_length=50)
    linked_symptoms = models.ManyToManyField(Symptom)
    periodicity = models.CharField(max_length=30)  # TODO this should be a choices or a database fk field maybe
    until = models.DateField()
