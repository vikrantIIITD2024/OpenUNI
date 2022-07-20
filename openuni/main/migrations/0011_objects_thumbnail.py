# Generated by Django 2.2.4 on 2022-07-02 13:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_images_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='objects',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]