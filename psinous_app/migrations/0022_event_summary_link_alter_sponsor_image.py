# Generated by Django 5.1.2 on 2024-11-28 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psinous_app', '0021_sponsor'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='summary_link',
            field=models.FileField(blank=True, null=True, upload_to='event_summaries/'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='sponsor/'),
        ),
    ]