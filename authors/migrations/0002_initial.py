# Generated by Django 4.0.3 on 2022-03-03 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, related_name='product', to='products.product'),
        ),
    ]
