from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView

from petlog.logger.models import Entry
from petlog.logger.forms import VaccineForm


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ["pet", "text"]
    template_name = 'logger/create_entry.html'

    def get_success_url(self):
        return reverse_lazy('home')


class FormCreateView(LoginRequiredMixin, FormView):
    form_class = VaccineForm
    template_name = 'logger/create_vaccine.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 400
        return response

    def get_success_url(self):
        return reverse_lazy('home')
