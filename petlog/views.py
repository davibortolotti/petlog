from django.shortcuts import render
from django.db.models import Value

from petlog.logger import models, forms


def home(request):
    entries = models.Entry.objects.all().order_by(
        '-created_on').annotate(type=Value('entry'))
    vaccines = models.Vaccine.objects.all().order_by(
        '-created_on').annotate(type=Value('vaccine'))
    events = list(entries) + list(vaccines)

    _forms = {
        "vaccine": forms.VaccineForm
    }
    events.sort(key=lambda x: x.created_on, reverse=True)
    context = {"events": events, "forms": _forms}
    return render(request, "home/home.html", context)
