# Generated by Django 4.0.3 on 2022-03-04 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0010_alter_author_avator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='avator',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.FileField(upload_to='profile_photos'),
        ),
    ]
