# Generated by Django 5.0.2 on 2024-02-26 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PopularPlaces",
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
                ("name", models.CharField(max_length=100)),
                ("price", models.IntegerField()),
                ("img", models.ImageField(upload_to="pics")),
                ("desc", models.TextField()),
                ("reviews", models.IntegerField()),
                ("days", models.IntegerField()),
            ],
        ),
    ]