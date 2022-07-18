# Generated by Django 4.0.1 on 2022-07-05 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_rename_price_jobadvert_name_jobadvert_pricemax_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobadvert',
            old_name='pricemax',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='freelancer',
            name='price',
        ),
        migrations.RemoveField(
            model_name='jobadvert',
            name='pricemin',
        ),
        migrations.RemoveField(
            model_name='jobadvert',
            name='procemid',
        ),
        migrations.AddField(
            model_name='freelancer',
            name='pricemax',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='pricemin',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='procemid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]