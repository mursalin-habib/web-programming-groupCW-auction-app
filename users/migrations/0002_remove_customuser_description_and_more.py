# Generated by Django 4.1.2 on 2022-12-13 03:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='description',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='status',
        ),
        migrations.AddField(
            model_name='customuser',
            name='dob',
            field=models.DateField(default=datetime.date(1997, 10, 19)),
        ),
    ]
