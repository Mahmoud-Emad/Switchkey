# Generated by Django 5.0.3 on 2024-04-03 23:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("switchkeys", "0003_alter_projectenvironment_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="environmentfeature",
            old_name="enabled_by_default",
            new_name="is_enabled",
        ),
        migrations.RenameField(
            model_name="environmentfeature",
            old_name="key",
            new_name="name",
        ),
        migrations.AlterUniqueTogether(
            name="environmentfeature",
            unique_together={("environment", "name", "value")},
        ),
        migrations.AlterField(
            model_name="environmentfeature",
            name="environment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="environment_features",
                to="switchkeys.projectenvironment",
            ),
        ),
        migrations.RemoveField(
            model_name="projectenvironmentuser",
            name="features",
        ),
        migrations.RemoveField(
            model_name="environmentfeature",
            name="description",
        ),
        migrations.RemoveField(
            model_name="environmentfeature",
            name="last_used",
        ),
        migrations.RemoveField(
            model_name="environmentfeature",
            name="tag",
        ),
        migrations.RemoveField(
            model_name="environmentfeature",
            name="tag_color",
        ),
        migrations.AddField(
            model_name="projectenvironmentuser",
            name="features",
            field=models.ManyToManyField(
                blank=True, to="switchkeys.environmentfeature"
            ),
        ),
    ]
