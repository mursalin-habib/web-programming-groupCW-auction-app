# Generated by Django 4.1.3 on 2022-12-14 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_customuser_city_alter_customuser_dob_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="profile_picture",
            field=models.ImageField(null=True, upload_to="media/"),
        ),
    ]