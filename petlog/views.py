from django.shortcuts import render
from django.db.models import Value

from petlog.logger import models


def home(request):
    
    entries = models.Entry.objects.all().order_by('-created_on').annotate(type=Value('entry'))
    vaccines = models.Vaccine.objects.all().order_by('-created_on').annotate(type=Value('vaccine'))
    events = list(entries) + list(vaccines)
    events.sort(key=lambda x: x.created_on, reverse=True)
    context = {"events": events}
    return render(request, "home/home.html", context)
