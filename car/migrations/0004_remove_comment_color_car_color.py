# Generated by Django 5.0.4 on 2024-05-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_comment_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='color',
        ),
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
