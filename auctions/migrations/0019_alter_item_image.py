# Generated by Django 4.1.3 on 2022-12-14 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0018_alter_item_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
