# Generated by Django 3.2.3 on 2021-06-10 15:00

from django.contrib.postgres.operations import AddIndexConcurrently
from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ("core", "0046_alter_janusserver_url"),
    ]

    operations = [
        AddIndexConcurrently(
            model_name="roomview",
            index=models.Index(fields=["start"], name="core_roomvi_start_0630ae_idx"),
        ),
    ]
