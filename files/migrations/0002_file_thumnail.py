# Generated by Django 4.0.3 on 2022-03-04 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='thumnail',
            field=models.FileField(blank=True, null=True, upload_to='profile_photos'),
        ),
    ]