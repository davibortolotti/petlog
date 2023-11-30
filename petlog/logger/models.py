import logging
from django.core.mail import send_mail
from django.db import models
from django.utils.timezone import now
from petlog.pets.models import Pet
from scheduler_field.fields import SchedulerDateField

logger = logging.getLogger(__name__)


class AbstractEntry(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField()
    created_on = models.DateTimeField(default=now)

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
    periodicity = models.CharField(null=True, max_length=30)  # TODO this should be a choices or a database fk field maybe
    until = models.DateField()


class TestModel(models.Model):
    name = models.CharField(max_length=20)
    reminder_date = SchedulerDateField(method_name='test_method')

    def test_method(_id):
        row = TestModel.objects.get(pk=_id)
        send_mail(
            "Subject here",
            f"HELLO {row.name}",
            "davibortolotti@gmail.com",
            ["davibortolotti@gmail.com"],
            fail_silently=False,
        )
