# Generated by Django 3.2.5 on 2021-07-14 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='body',
        ),
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
