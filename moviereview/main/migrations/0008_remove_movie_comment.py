# Generated by Django 4.2.3 on 2023-08-01 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_movie_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='comment',
        ),
    ]