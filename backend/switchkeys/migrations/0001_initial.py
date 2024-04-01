# Generated by Django 5.0.3 on 2024-04-01 11:19

import django.db.models.deletion
import switchkeys.utils.generates
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("first_name", models.CharField(max_length=45)),
                ("last_name", models.CharField(max_length=45)),
                ("email", models.EmailField(max_length=45, unique=True)),
                (
                    "background_color",
                    models.CharField(
                        default=switchkeys.utils.generates.generate_random_color,
                        max_length=10,
                    ),
                ),
                ("joining_at", models.DateField(auto_now_add=True)),
                (
                    "user_type",
                    models.CharField(
                        choices=[("Administrator", "administrator"), ("User", "user")],
                        default="Administrator",
                        max_length=20,
                    ),
                ),
                ("is_admin", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ProjectEnvironmentUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("username", models.CharField(max_length=30, unique=True)),
                ("features", models.JSONField(blank=True, default=dict)),
            ],
            options={
                "verbose_name": "Project User",
                "verbose_name_plural": "Project User",
            },
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=20)),
                (
                    "members",
                    models.ManyToManyField(
                        blank=True,
                        related_name="organization_members",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organization_owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Organization",
                "verbose_name_plural": "Organizations",
                "unique_together": {("name", "owner")},
            },
        ),
        migrations.CreateModel(
            name="OrganizationProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=20)),
                (
                    "organization",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project_organization",
                        to="switchkeys.organization",
                    ),
                ),
            ],
            options={
                "verbose_name": "Organization Project",
                "verbose_name_plural": "Organization Projects",
                "unique_together": {("name", "organization")},
            },
        ),
        migrations.CreateModel(
            name="ProjectEnvironment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=50)),
                (
                    "environment_key",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                (
                    "project",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="environment_project",
                        to="switchkeys.organizationproject",
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(
                        blank=True,
                        related_name="environment_users",
                        to="switchkeys.projectenvironmentuser",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UserDevice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "device_type",
                    models.CharField(
                        choices=[("IPhone", "iPhone"), ("Android", "Android")],
                        default="Android",
                        max_length=20,
                    ),
                ),
                ("version", models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                "verbose_name": "User Device",
                "verbose_name_plural": "User Device",
                "unique_together": {("device_type", "version")},
            },
        ),
        migrations.AddField(
            model_name="projectenvironmentuser",
            name="device",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="user_device",
                to="switchkeys.userdevice",
            ),
        ),
        migrations.CreateModel(
            name="OrganizationProjectGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=50)),
                (
                    "members",
                    models.ManyToManyField(
                        related_name="organization_groups", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project_groups",
                        to="switchkeys.organizationproject",
                    ),
                ),
            ],
            options={
                "verbose_name": "Organization Project Group",
                "verbose_name_plural": "Organization Project Groups",
                "unique_together": {("name", "project")},
            },
        ),
        migrations.CreateModel(
            name="EnvironmentFeature",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("key", models.CharField(max_length=20)),
                ("value", models.TextField(max_length=750)),
                ("tag", models.CharField(blank=True, max_length=20, null=True)),
                ("tag_color", models.CharField(blank=True, max_length=25, null=True)),
                (
                    "description",
                    models.TextField(blank=True, max_length=750, null=True),
                ),
                ("enabled_by_default", models.BooleanField(default=False)),
                ("is_default", models.BooleanField(default=False)),
                ("last_used", models.DateTimeField(auto_now=True)),
                (
                    "environment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="environment_keys",
                        to="switchkeys.projectenvironment",
                    ),
                ),
            ],
            options={
                "verbose_name": "Environment Feature",
                "verbose_name_plural": "Environment Features",
                "unique_together": {("environment", "key")},
            },
        ),
    ]