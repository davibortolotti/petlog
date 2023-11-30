FROM python:3.9
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
