# Generated by Django 4.0.3 on 2022-03-04 07:53

import authors.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0009_alter_author_avatar_thumbnail_alter_author_avator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='avator',
            field=models.FileField(upload_to=authors.models.mainImage_path),
        ),
    ]
