# Generated by Django 4.2.3 on 2023-08-04 04:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0013_alter_profile_bio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(default="default.webp", upload_to="profile_pics"),
        ),
    ]