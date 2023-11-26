from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from petlog.logger.models import Entry


class EntryCreateView(CreateView):
    model = Entry
    fields = ["pet", "text"]
    template_name = 'logger/create_entry.html'

    def get_success_url(self):
        return reverse_lazy('home')
