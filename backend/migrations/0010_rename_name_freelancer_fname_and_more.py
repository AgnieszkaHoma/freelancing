# Generated by Django 4.0.1 on 2022-07-05 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_remove_jobadvert_name_remove_jobadvert_surname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freelancer',
            old_name='name',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='freelancer',
            old_name='surname',
            new_name='lname',
        ),
    ]
