# Generated by Django 4.1.3 on 2022-12-04 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_alter_newarrivals_main_display'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=300, null=True)),
                ('Sub_heading', models.CharField(max_length=300, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Blog_Image', models.ImageField(blank=True, null=True, upload_to='files/BlogImages')),
                ('Street', models.CharField(max_length=300, null=True)),
                ('Suburb', models.CharField(max_length=300, null=True)),
                ('City_Town', models.CharField(max_length=300, null=True)),
                ('Province', models.CharField(max_length=300, null=True)),
                ('Event_TimeStart', models.CharField(max_length=300, null=True)),
                ('Event_TimeEnd', models.CharField(max_length=300, null=True)),
                ('Event_Startdate', models.DateField(blank=True, null=True)),
                ('Event_EndDate', models.DateField(blank=True, null=True)),
                ('LinkOne', models.CharField(max_length=1000, null=True)),
                ('LinkTwo', models.CharField(max_length=1000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
