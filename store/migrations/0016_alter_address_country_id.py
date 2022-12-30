# Generated by Django 4.1.3 on 2022-12-23 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0015_alter_address_country_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="country_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="store.country",
            ),
        ),
    ]