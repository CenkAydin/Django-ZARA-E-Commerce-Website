# Generated by Django 4.1.3 on 2022-12-23 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0012_alter_order_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer_Address",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("is_default", models.BooleanField(default=False)),
                (
                    "address_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.address",
                    ),
                ),
                (
                    "customer_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.customer",
                    ),
                ),
            ],
        ),
    ]
