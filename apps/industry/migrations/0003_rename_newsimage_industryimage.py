# Generated by Django 4.2.9 on 2024-01-15 06:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("industry", "0002_newsimage"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="NewsImage",
            new_name="IndustryImage",
        ),
    ]
