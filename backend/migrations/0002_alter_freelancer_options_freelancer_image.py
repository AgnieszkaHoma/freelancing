# Generated by Django 4.0.5 on 2022-07-04 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='freelancer',
            options={'ordering': ['-published']},
        ),
        migrations.AddField(
            model_name='freelancer',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]