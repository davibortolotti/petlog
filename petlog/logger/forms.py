from django.forms import ModelForm
from petlog.logger.models import Vaccine, Entry, Training, Symptom


class VaccineForm(ModelForm):
    class Meta:
        model = Vaccine
        fields = [
            "text", "vaccine_type", "given_on", "given_at", "given_by", "next_dose", "pet"
        ]
