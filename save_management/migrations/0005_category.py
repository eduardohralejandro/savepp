# Generated by Django 4.2.4 on 2023-09-04 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("save_management", "0004_transaction"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="category_id",
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("title", models.TextField()),
                (
                    "bill_id_on_category",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bill_id_on_category",
                        to="save_management.bill",
                    ),
                ),
            ],
        ),
    ]
