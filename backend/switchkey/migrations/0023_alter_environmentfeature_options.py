# Generated by Django 5.0.3 on 2024-03-31 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("switchkey", "0022_rename_featurestorage_environmentfeature"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="environmentfeature",
            options={
                "verbose_name": "Environment Feature",
                "verbose_name_plural": "Environment Features",
            },
        ),
    ]