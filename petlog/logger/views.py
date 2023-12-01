from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from petlog.logger.forms import EntryForm, VaccineForm, TrainingForm

class HomeViewMixin:
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 400
        return response

    def get_success_url(self):
        return reverse_lazy('home')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class EntryCreateView(HomeViewMixin, LoginRequiredMixin, FormView):
    form_class = EntryForm
    template_name = 'logger/create_entry.html'


class TrainingCreateView(HomeViewMixin, LoginRequiredMixin, FormView):
    form_class = TrainingForm
    template_name = 'logger/create_training.html'


class VaccineCreateView(HomeViewMixin, LoginRequiredMixin, FormView):
    form_class = VaccineForm
    template_name = 'logger/create_vaccine.html'

