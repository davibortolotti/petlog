from django.contrib.auth.decorators import login_required
from django.db.models import Value
from django.shortcuts import render

from petlog.logger import models, forms


@login_required
def home(request):
    entries = models.Entry.objects.filter(pet__guardian=request.user).order_by(
        '-created_on').annotate(type=Value('entry'))
    vaccines = models.Vaccine.objects.filter(pet__guardian=request.user).order_by(
        '-created_on').annotate(type=Value('vaccine'))
    training = models.Training.objects.filter(pet__guardian=request.user).order_by(
        '-created_on').annotate(type=Value('training'))
    events = list(entries) + list(vaccines) + list(training)

    events.sort(key=lambda x: x.created_on, reverse=True)
    context = {"events": events, "user": request.user}
    return render(request, "home/home.html", context)
