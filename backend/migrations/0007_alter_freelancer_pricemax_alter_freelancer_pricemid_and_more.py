# Generated by Django 4.0.1 on 2022-07-05 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_rename_procemid_freelancer_pricemid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='pricemax',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='pricemid',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='pricemin',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]