## CReate a management command that polls the database for the date field and executes the function based on itfrom django.apps import apps
from django.apps import apps

from scheduler_field.models import SchedulerDateManager

def get_model_by_db_table(db_table):
    for model in apps.get_models():
        if model._meta.db_table == db_table:
            return model
    else:
        raise ValueError('No model found with db_table {}!'.format(db_table))


def run_function_for_date(datetime):
    for row in SchedulerDateManager.objects.all():
        model = get_model_by_db_table(row.table_name)
        due_entries = model.objects.filter(**{row.field_name: datetime})
        for i in due_entries:
            getattr(model, row.method_name)(i.pk)
