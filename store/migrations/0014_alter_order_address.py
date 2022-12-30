# Generated by Django 4.1.3 on 2022-12-23 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0013_customer_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="address",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="store.address",
            ),
        ),
    ]