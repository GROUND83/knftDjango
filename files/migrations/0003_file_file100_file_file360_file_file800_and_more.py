# Generated by Django 4.0.3 on 2022-03-04 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_file_thumnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file100',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='file',
            name='file360',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='file',
            name='file800',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='file',
            name='thumnail',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
