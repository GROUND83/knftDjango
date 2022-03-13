# Generated by Django 4.0.3 on 2022-03-04 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_file_author'),
        ('authors', '0018_remove_author_avator'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='avator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='files.file'),
        ),
    ]
