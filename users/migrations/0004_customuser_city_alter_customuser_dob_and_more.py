# Generated by Django 4.1.3 on 2022-12-14 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_customuser_profile_picture"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="city",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="dob",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="profile_picture",
            field=models.ImageField(upload_to="media/"),
        ),
    ]
