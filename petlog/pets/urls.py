from django.urls import path

from petlog.pets import views


urlpatterns = [
    path("", views.list_pets, name='list_pets'),
    path("create/", views.PetCreateView.as_view(), name='create_pet')
]
