# Generated by Django 4.1.3 on 2022-12-14 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0017_remove_item_category_remove_item_img_url_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="static/img/"),
        ),
    ]
