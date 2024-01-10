# Generated by Django 4.2.9 on 2024-01-10 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("program", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="program",
            name="cover",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="wagtailimages.image",
                verbose_name="커버",
            ),
        ),
    ]
