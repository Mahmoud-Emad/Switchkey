# Generated by Django 5.0.3 on 2024-03-28 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("switchkey", "0008_remove_organizationproject_environments_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="organization",
            name="projects",
        ),
        migrations.AddField(
            model_name="organizationproject",
            name="organization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="project_organization",
                to="switchkey.organization",
            ),
        ),
        migrations.RemoveField(
            model_name="projectenvironment",
            name="project",
        ),
        migrations.AddField(
            model_name="projectenvironment",
            name="project",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="environment_project",
                to="switchkey.organizationproject",
            ),
        ),
    ]