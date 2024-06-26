# Generated by Django 4.2.11 on 2024-03-29 06:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('desc', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 3, 29, 6, 4, 55, 1080)),
        ),
    ]
