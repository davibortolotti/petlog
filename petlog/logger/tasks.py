from django.utils.timezone import now
from scheduler_field.commands import run_function_for_date

from petlog.celery import app


@app.task(bind=True, ignore_result=True)
def run_functions_for_date(self):
    print("running task", now())
    run_function_for_date(now())
