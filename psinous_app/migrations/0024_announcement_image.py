# Generated by Django 5.1.2 on 2024-11-29 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psinous_app', '0023_remove_announcement_image_announcement_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='announcement/'),
        ),
    ]
