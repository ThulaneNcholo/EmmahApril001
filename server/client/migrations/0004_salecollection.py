# Generated by Django 4.1.3 on 2022-12-03 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sale_Price', models.FloatField(blank=True, null=True)),
                ('End_date', models.DateField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Product', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sale_collection', to='client.product')),
            ],
        ),
    ]
