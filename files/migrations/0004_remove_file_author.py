# Generated by Django 4.0.3 on 2022-03-04 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_file_file100_file_file360_file_file800_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='author',
        ),
    ]
