# Generated by Django 3.2.5 on 2021-08-07 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_remove_articles_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='image',
        ),
    ]
