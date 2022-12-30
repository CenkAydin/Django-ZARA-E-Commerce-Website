# Generated by Django 4.1.3 on 2022-12-22 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0006_order_status"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "categories"},
        ),
        migrations.AddField(
            model_name="category",
            name="parent2",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to="store.category",
            ),
        ),
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(default=models.CharField(max_length=50)),
        ),
        migrations.AlterUniqueTogether(
            name="category",
            unique_together={("slug", "parent2")},
        ),
    ]
