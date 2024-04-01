# Generated by Django 5.0.3 on 2024-03-28 11:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("switchkey", "0006_alter_organizationproject_environments_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organizationproject",
            name="team",
            field=models.ManyToManyField(
                blank=True, related_name="project_team", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]