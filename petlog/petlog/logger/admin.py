from django.contrib import admin
from petlog.logger import models

admin.site.register(models.Entry)
admin.site.register(models.Medicine)
admin.site.register(models.Symptom)
admin.site.register(models.Training)
admin.site.register(models.Vaccine)
