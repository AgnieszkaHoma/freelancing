# Generated by Django 4.0.1 on 2022-07-05 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_alter_freelancer_pricemax_alter_freelancer_pricemid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freelancer',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='freelancer',
            name='lname',
        ),
    ]