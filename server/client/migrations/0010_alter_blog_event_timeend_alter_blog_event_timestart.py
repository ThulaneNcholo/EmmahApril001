# Generated by Django 4.1.3 on 2022-12-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Event_TimeEnd',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='Event_TimeStart',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
