# Generated by Django 4.2.8 on 2023-12-15 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tile",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Warehouse",
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
                ("name", models.CharField(max_length=100, unique=True)),
                ("location", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Inventory",
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
                ("quantity", models.PositiveIntegerField()),
                (
                    "tile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tile_inventory_api.tile",
                    ),
                ),
                (
                    "warehouse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tile_inventory_api.warehouse",
                    ),
                ),
            ],
            options={"unique_together": {("tile", "warehouse")},},
        ),
    ]