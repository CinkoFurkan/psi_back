# Generated by Django 5.1.2 on 2024-11-29 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psinous_app', '0024_announcement_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberYear',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(max_length=9)),
                ('members', models.ManyToManyField(related_name='member_years', to='psinous_app.member')),
            ],
        ),
    ]