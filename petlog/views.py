from django.contrib.auth.decorators import login_required
from django.db.models import Value
from django.shortcuts import render

from petlog.logger import models, forms


@login_required
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
    context = {"events": events, "forms": _forms, "user": request.user}
    return render(request, "home/home.html", context)
