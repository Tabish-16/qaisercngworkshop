# Generated by Django 5.0.7 on 2024-08-31 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OilTraders', '0015_ac_filter_air_filter_oil_filter_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whole_Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('purchase_price', models.CharField(blank=True, max_length=200, null=True)),
                ('sale_price', models.CharField(blank=True, max_length=200, null=True)),
                ('profit', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='newentry',
            name='wholeSaleEntry',
            field=models.JSONField(default=dict, null=True),
        ),
    ]
