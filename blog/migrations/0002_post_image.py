# Generated by Django 4.2.3 on 2023-07-23 04:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="post_pics"),
        ),
    ]
