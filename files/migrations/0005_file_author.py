# Generated by Django 4.0.3 on 2022-03-04 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0018_remove_author_avator'),
        ('files', '0004_remove_file_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='authors.author'),
        ),
    ]
