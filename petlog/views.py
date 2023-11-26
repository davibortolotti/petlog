from django.shortcuts import render

from petlog.logger import models


def home(request):
    entries = models.Entry.objects.all().order_by('-created_on')
    context = {"entries": entries}
    return render(request, "home/home.html", context)
