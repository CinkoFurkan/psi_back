# Generated by Django 5.1.2 on 2024-12-05 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psinous_app', '0027_remove_event_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='position',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]