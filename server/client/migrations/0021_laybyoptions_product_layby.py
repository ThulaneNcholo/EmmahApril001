# Generated by Django 4.1.3 on 2022-12-05 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0020_alter_cartitems_satus'),
    ]

    operations = [
        migrations.CreateModel(
            name='LayByOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Yes', max_length=100, null=True)),
                ('Monthsdata', models.IntegerField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='layby',
            field=models.ManyToManyField(blank=True, default=None, related_name='layBy_options', to='client.laybyoptions'),
        ),
    ]
