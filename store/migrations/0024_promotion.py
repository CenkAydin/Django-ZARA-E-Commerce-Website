# Generated by Django 4.1.3 on 2022-12-23 15:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0023_payment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Promotion",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=50)),
                ("discount_rate", models.IntegerField(default=0)),
                ("start_date", models.DateField(default=datetime.datetime.today)),
                ("end_date", models.DateField(default=datetime.datetime.today)),
                (
                    "category_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.category",
                    ),
                ),
            ],
        ),
    ]
