# Generated by Django 4.0.1 on 2022-07-05 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_freelancer_options_freelancer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
