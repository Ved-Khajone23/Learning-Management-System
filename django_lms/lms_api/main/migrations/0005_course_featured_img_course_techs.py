# Generated by Django 5.0.4 on 2024-04-27 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_teacher_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="featured_img",
            field=models.ImageField(null=True, upload_to="course_imgs/"),
        ),
        migrations.AddField(
            model_name="course",
            name="techs",
            field=models.TextField(null=True),
        ),
    ]