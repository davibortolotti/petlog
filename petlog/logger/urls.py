from django.urls import path

from petlog.logger import views


urlpatterns = [
    path("create_entry/", views.EntryCreateView.as_view(), name='create_entry'),
    path("create_vaccine/", views.VaccineCreateView.as_view(), name='create_vaccine'),
    path("create_training/", views.TrainingCreateView.as_view(), name='create_training')
]
