# Generated by Django 4.1.3 on 2022-12-04 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_alter_salecollection_main_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newarrivals',
            name='main_display',
            field=models.CharField(choices=[('First', 'First'), ('second', 'second'), ('third', 'third')], default='No', max_length=10),
        ),
    ]
