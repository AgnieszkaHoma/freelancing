# Generated by Django 4.0.1 on 2022-07-08 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_rename_fname_freelancer_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer',
            name='deliveryDaysForPriceextra',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='deliveryDaysForPricemax',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='deliveryDaysForPricemid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='deliveryDaysForPricemin',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
