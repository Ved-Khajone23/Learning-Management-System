# Generated by Django 5.0.4 on 2024-04-29 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_alter_chapter_course_alter_course_teacher"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="detail",
            field=models.TextField(null=True),
        ),
    ]
