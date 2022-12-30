# Generated by Django 4.1.3 on 2022-12-23 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0021_shopping_cart"),
    ]

    operations = [
        migrations.CreateModel(
            name="Shoping_Cart_Item",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("quantity", models.IntegerField(default=1)),
                (
                    "product_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.products",
                    ),
                ),
                (
                    "shopping_cart_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.shopping_cart",
                    ),
                ),
            ],
        ),
    ]