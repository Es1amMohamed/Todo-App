# Generated by Django 4.2.5 on 2023-11-27 19:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="title",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
