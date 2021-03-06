# Generated by Django 4.0.3 on 2022-03-05 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_product_image100_remove_product_image200_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='작품 설명'),
        ),
        migrations.AlterField(
            model_name='product',
            name='dimensionsx',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='x 사이즈'),
        ),
        migrations.AlterField(
            model_name='product',
            name='dimensionsy',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='y 사이즈'),
        ),
        migrations.AlterField(
            model_name='product',
            name='edtionTitle',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='edtion title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='foundataionLink',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='foundataionLink'),
        ),
        migrations.AlterField(
            model_name='product',
            name='openseaLink',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='openseaLink'),
        ),
        migrations.AlterField(
            model_name='product',
            name='otherTitle',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='other title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='projectTitle',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='project title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='raribleLink',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='raribleLink'),
        ),
        migrations.AlterField(
            model_name='product',
            name='solahartLink',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='solahartLink'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='products.tag', verbose_name='tag'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='작품 타이틀'),
        ),
    ]
