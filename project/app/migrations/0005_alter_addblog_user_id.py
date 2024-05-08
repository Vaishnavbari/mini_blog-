# Generated by Django 5.0.2 on 2024-02-20 09:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_addblog_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addblog',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
