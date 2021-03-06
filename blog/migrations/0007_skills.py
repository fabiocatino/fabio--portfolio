# Generated by Django 3.2.5 on 2021-07-11 08:31

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210316_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=256)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('level', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
            ],
        ),
    ]
