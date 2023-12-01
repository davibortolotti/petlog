from django.forms import ModelForm, ModelChoiceField, Select, DateInput, TextInput, Textarea, CheckboxInput
from petlog.logger.models import Vaccine, Entry, Training
from petlog.pets.models import Pet


class DateInput(DateInput):
    input_type = 'date'


class PetChoiceMixin():
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pet'] = ModelChoiceField(
            queryset=Pet.objects.filter(guardian=user),
            widget=Select(attrs={'class': 'form-control select2'})
        )


class VaccineForm(PetChoiceMixin, ModelForm):
    class Meta:
        model = Vaccine
        fields = [
            "pet", "vaccine_type", "given_on", "given_at", "given_by", "next_dose", "remind_me", "text"
        ]
        widgets = {
            'vaccine_type': TextInput(attrs={'class': 'form-control'}),
            'given_by': TextInput(attrs={'class': 'form-control'}),
            'given_at': TextInput(attrs={'class': 'form-control'}),
            'given_on': DateInput(attrs={'class': 'form-control'}),
            'next_dose': DateInput(attrs={'class': 'form-control'}),
            'remind_me': CheckboxInput(attrs={'class': 'form-check-input'}),
            'text': Textarea(attrs={'class': 'form-control'}),
        }


class EntryForm(PetChoiceMixin, ModelForm):
    class Meta:
        model = Entry
        fields = [
            "pet", "text"
        ]
        widgets = {
            'text': Textarea(attrs={'class': 'form-control'}),
        }


class TrainingForm(PetChoiceMixin, ModelForm):
    class Meta:
        model = Training
        fields = [
            "pet", "text"
        ]
        widgets = {
            'text': Textarea(attrs={'class': 'form-control'}),
        }
