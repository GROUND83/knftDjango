# Generated by Django 4.0.3 on 2022-03-04 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0004_rename_avator100_author_avator_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='avatar_thumbnail',
            field=models.ImageField(blank=True, upload_to='profile_photos/thum'),
        ),
    ]