# Generated by Django 4.1.7 on 2023-04-05 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0012_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_released',
            field=models.DateTimeField(blank=True),
        ),
    ]