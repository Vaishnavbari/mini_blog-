# Generated by Django 5.0.2 on 2024-02-12 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]