# Generated by Django 5.1.2 on 2024-11-28 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psinous_app', '0020_member_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]