# Generated by Django 4.2.3 on 2023-08-03 03:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0008_alter_profile_bio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="bio",
            field=models.TextField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name="profile",
            name="location",
            field=models.CharField(max_length=100),
        ),
    ]
