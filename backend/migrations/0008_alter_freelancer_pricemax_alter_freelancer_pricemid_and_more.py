# Generated by Django 4.0.1 on 2022-07-05 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_alter_freelancer_pricemax_alter_freelancer_pricemid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='pricemax',
            field=models.DecimalField(decimal_places=2, default='Price per hour', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='pricemid',
            field=models.DecimalField(decimal_places=2, default='Price per hour', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='pricemin',
            field=models.DecimalField(decimal_places=2, default='Price per hour', max_digits=10, null=True),
        ),
    ]
