# Generated by Django 3.2.5 on 2021-07-18 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_alter_comments_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='preview',
        ),
    ]
