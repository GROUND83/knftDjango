# Generated by Django 4.0.3 on 2022-03-05 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_creationdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='projectType',
            field=models.CharField(blank=True, choices=[('the Love', 'the Love'), ('the Load', 'the Load')], default='the Love', max_length=40, null=True, verbose_name='project type'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productType',
            field=models.CharField(blank=True, choices=[('project', 'project'), ('edition', 'edition'), ('other', 'other')], default='project', max_length=40, null=True, verbose_name='product type'),
        ),
    ]
