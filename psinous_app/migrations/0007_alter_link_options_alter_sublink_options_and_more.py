# Generated by Django 5.1.1 on 2024-10-31 08:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("psinous_app", "0006_announcement"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="link",
            options={"ordering": ["position"]},
        ),
        migrations.AlterModelOptions(
            name="sublink",
            options={"ordering": ["position"]},
        ),
        migrations.AddField(
            model_name="link",
            name="position",
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="sublink",
            name="position",
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
