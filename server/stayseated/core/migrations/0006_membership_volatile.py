# Generated by Django 3.0.5 on 2020-04-24 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_membership"),
    ]

    operations = [
        migrations.AddField(
            model_name="membership",
            name="volatile",
            field=models.BooleanField(default=False),
        ),
    ]
