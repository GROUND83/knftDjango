# Generated by Django 4.0.3 on 2022-03-03 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name='작가명')),
                ('authDes', models.CharField(max_length=50, null=True, verbose_name='작가설명')),
                ('avator50', models.ImageField(blank=True, upload_to='profile_photos')),
                ('avator100', models.ImageField(blank=True, upload_to='profile_photos')),
                ('desTitle', models.CharField(max_length=50, null=True, verbose_name='작가 타이틀')),
                ('description', models.CharField(max_length=50, null=True, verbose_name='작가 컨텐츠')),
                ('discord', models.CharField(max_length=50, null=True, verbose_name='discord')),
                ('facebook', models.CharField(max_length=50, null=True, verbose_name='facebook')),
                ('instargram', models.CharField(max_length=50, null=True, verbose_name='instargram')),
                ('twitter', models.CharField(max_length=50, null=True, verbose_name='twitter')),
                ('show', models.BooleanField(default=True, verbose_name='노출')),
            ],
            options={
                'verbose_name': '작가',
                'verbose_name_plural': '작가모음',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('caption', models.CharField(max_length=80, verbose_name='사진이름')),
                ('file', models.ImageField(upload_to='profile_photos')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='authors.author')),
            ],
            options={
                'verbose_name': '프로필사진',
                'verbose_name_plural': '프로필사진 모음',
            },
        ),
    ]
