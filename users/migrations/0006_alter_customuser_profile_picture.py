# Generated by Django 4.1.3 on 2022-12-14 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_customuser_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="profile_picture",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
    ]
