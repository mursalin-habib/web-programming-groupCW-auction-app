# Generated by Django 4.1.2 on 2022-12-13 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_customuser_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='default.png', upload_to='uploads/'),
        ),
    ]
