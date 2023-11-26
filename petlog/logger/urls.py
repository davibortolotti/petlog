from django.urls import path

from petlog.logger import views


urlpatterns = [
    path("create/", views.EntryCreateView.as_view(), name='create_entry')
]
