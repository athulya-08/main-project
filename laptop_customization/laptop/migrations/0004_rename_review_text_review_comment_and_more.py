# Generated by Django 5.1 on 2024-08-29 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0003_remove_laptop_image_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review_text',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='review',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='review',
            name='laptop',
        ),
    ]