# Generated by Django 3.1.1 on 2023-03-13 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20230313_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='item_images'),
        ),
    ]
