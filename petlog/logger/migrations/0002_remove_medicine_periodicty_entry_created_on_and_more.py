# Generated by Django 4.2.7 on 2023-11-25 17:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("logger", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="medicine",
            name="periodicty",
        ),
        migrations.AddField(
            model_name="entry",
            name="created_on",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 25, 17, 41, 45, 321790, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AddField(
            model_name="medicine",
            name="created_on",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 25, 17, 41, 45, 321790, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AddField(
            model_name="medicine",
            name="periodicity",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="symptom",
            name="created_on",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 25, 17, 41, 45, 321790, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AddField(
            model_name="training",
            name="created_on",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 25, 17, 41, 45, 321790, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AddField(
            model_name="vaccine",
            name="created_on",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 25, 17, 41, 45, 321790, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="vaccine",
            name="given_by",
            field=models.CharField(max_length=30),
        ),
    ]