# Generated by Django 4.1.3 on 2022-12-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0018_rename_category_deliveryoption_useritems'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryoption',
            name='object_Name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
