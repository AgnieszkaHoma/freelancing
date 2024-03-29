# Generated by Django 4.0.1 on 2022-07-06 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0015_alter_freelancer_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('introduceYourself', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='backend.freelancer')),
            ],
        ),
    ]
