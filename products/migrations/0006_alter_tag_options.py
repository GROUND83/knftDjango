# Generated by Django 4.0.3 on 2022-03-05 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_tag_alter_product_description_alter_product_image100_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': 'Tags'},
        ),
    ]
