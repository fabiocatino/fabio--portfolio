# Generated by Django 3.2.5 on 2021-07-24 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_remove_articles_likes'),
        ('portfolio', '0009_alter_items_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='tags',
            field=models.ManyToManyField(blank=True, max_length=100, to='blog.Skills'),
        ),
    ]
