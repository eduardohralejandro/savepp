# Generated by Django 4.2.4 on 2023-09-04 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("save_management", "0002_remove_extendeduser_created"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bill",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="bill_id",
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("title", models.TextField()),
                ("amount", models.IntegerField()),
                ("note", models.TextField(blank=True, null=True)),
                ("document", models.TextField(blank=True, null=True)),
                ("settled", models.BooleanField(default=False)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "bill_created_by_user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
