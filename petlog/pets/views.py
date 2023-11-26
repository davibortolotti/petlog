from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from petlog.pets.models import Pet


def list_pets(request):
    pets = Pet.objects.filter(guardian=request.user).order_by('-created_on')
    context = {"pets": pets}

    return render(request, "pets/index.html", context)


class PetCreateView(CreateView):
    model = Pet
    fields = ["name", "species", "breed", "color", "date_of_birth"]
    template_name = 'pets/create.html'

    def get_success_url(self):
        return reverse_lazy('list_pets')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.guardian = self.request.user
        obj.save()
        return HttpResponseRedirect(self.get_success_url())
