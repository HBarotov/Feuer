# Generated by Django 4.2.3 on 2023-08-03 04:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0010_alter_profile_bio_alter_profile_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="bio",
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
