# Generated by Django 4.0.3 on 2022-03-04 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0006_alter_author_avator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='avator',
            field=models.ImageField(blank=True, upload_to='profile_photos'),
        ),
    ]