# Generated by Django 4.0.3 on 2022-03-04 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0016_alter_author_avator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='avatar_thumbnail',
        ),
    ]
