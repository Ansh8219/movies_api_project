# Generated by Django 5.0 on 2024-02-06 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StreamPlatform",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("about", models.CharField(max_length=50)),
                ("website", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="WatchList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("storyline", models.CharField(max_length=150)),
                ("active", models.BooleanField(default=True)),
                ("creted", models.DateField(auto_now_add=True)),
                (
                    "platform",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apk.streamplatform",
                    ),
                ),
            ],
        ),
    ]
