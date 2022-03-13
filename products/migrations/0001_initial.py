# Generated by Django 4.0.3 on 2022-03-03 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, null=True, verbose_name='작품타이틀')),
                ('description', models.CharField(max_length=300, null=True, verbose_name='작품설명')),
                ('creationDate', models.DateTimeField(blank=True, null=True)),
                ('type', models.CharField(blank=True, choices=[('Notable', 'Notable'), ('Caligraphy', 'Caligraphy'), ('Engraving', 'Engraving'), ('Illustration', 'Illustration'), ('Photography', 'Photography')], default='Caligraphy', max_length=40, null=True, verbose_name='type')),
                ('dimensionsx', models.CharField(max_length=10, null=True, verbose_name='x 사이즈')),
                ('dimensionsy', models.CharField(max_length=10, null=True, verbose_name='y 사이즈')),
                ('productType', models.CharField(blank=True, choices=[('the Love', 'the Love'), ('the Load', 'the Load')], default='the Love', max_length=40, null=True, verbose_name='type')),
                ('projectTitle', models.CharField(max_length=100, null=True, verbose_name='project title')),
                ('edtionTitle', models.CharField(max_length=100, null=True, verbose_name='edtion title')),
                ('otherTitle', models.CharField(max_length=100, null=True, verbose_name='other title')),
                ('foundataionLink', models.CharField(max_length=50, null=True, verbose_name='foundataionLink')),
                ('openseaLink', models.CharField(max_length=50, null=True, verbose_name='openseaLink')),
                ('solahartLink', models.CharField(max_length=50, null=True, verbose_name='solahartLink')),
                ('raribleLink', models.CharField(max_length=50, null=True, verbose_name='raribleLink')),
                ('image', models.CharField(max_length=300, null=True, verbose_name='image')),
                ('image100', models.CharField(max_length=300, null=True, verbose_name='image100')),
                ('image200', models.CharField(max_length=300, null=True, verbose_name='image200')),
                ('image400', models.CharField(max_length=300, null=True, verbose_name='image400')),
                ('image800', models.CharField(max_length=300, null=True, verbose_name='image800')),
                ('main', models.BooleanField(default=False, verbose_name='메인노출')),
                ('number', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='작품넘버')),
                ('hit', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='hit')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='ETH 가격')),
                ('tags', models.CharField(max_length=300, null=True, verbose_name='tags')),
                ('theme', models.CharField(max_length=100, null=True, verbose_name='theme')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='authors.author')),
            ],
            options={
                'verbose_name': '작품',
                'verbose_name_plural': '작품',
                'ordering': ['title'],
            },
        ),
    ]