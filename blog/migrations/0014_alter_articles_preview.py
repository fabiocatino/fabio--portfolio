# Generated by Django 3.2.5 on 2021-07-12 12:53

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_articles_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='preview',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=178),
        ),
    ]
