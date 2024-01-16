# Generated by Django 4.2.9 on 2024-01-15 05:49

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0007_blog_subtitle"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="subtitle",
            field=wagtail.fields.StreamField(
                [
                    (
                        "subtitle",
                        wagtail.blocks.RichTextBlock(label="소제목", required=False),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
                verbose_name="내용",
            ),
        ),
    ]
