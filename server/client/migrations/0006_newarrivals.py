# Generated by Django 4.1.3 on 2022-12-03 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_product_main_display_salecollection_main_display'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewArrivals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sale_Price', models.FloatField(blank=True, null=True)),
                ('End_date', models.DateField(blank=True, null=True)),
                ('main_display', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Product', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='new_arrivals', to='client.product')),
            ],
        ),
    ]
