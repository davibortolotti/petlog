# Generated by Django 4.2.7 on 2023-11-30 23:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('vaccine_type', models.CharField(max_length=30)),
                ('given_on', models.DateField()),
                ('given_at', models.CharField(max_length=30)),
                ('given_by', models.CharField(max_length=30)),
                ('remind_me', models.BooleanField(default=False)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=50)),
                ('periodicity', models.CharField(max_length=30, null=True)),
                ('until', models.DateField()),
                ('linked_symptoms', models.ManyToManyField(to='logger.symptom')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
