# Generated by Django 4.1.3 on 2022-12-04 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0010_alter_blog_event_timeend_alter_blog_event_timestart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Event_TimeEnd',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='Event_TimeStart',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
