# Generated by Django 4.0.3 on 2022-03-04 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0013_file_content_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'verbose_name': '파일', 'verbose_name_plural': '파일모음'},
        ),
    ]
