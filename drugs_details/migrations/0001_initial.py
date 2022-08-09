# Generated by Django 4.1 on 2022-08-08 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Drug",
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
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("sku", models.CharField(max_length=200)),
                ("price", models.IntegerField()),
                ("image", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name_plural": "drugs",
            },
        ),
    ]
