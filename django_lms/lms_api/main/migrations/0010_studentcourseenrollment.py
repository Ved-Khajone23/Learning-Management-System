# Generated by Django 5.0.4 on 2024-04-29 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0009_rename_qualification_student_username_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentCourseEnrollment",
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
                ("enrolled_time", models.DateTimeField(auto_now_add=True)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="enrolled_courses",
                        to="main.course",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="enrolled_student",
                        to="main.student",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "6. Enrolled Courses",
            },
        ),
    ]
