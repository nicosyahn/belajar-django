# Generated by Django 2.2.12 on 2022-11-20 16:23

import dashboard.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_membership_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='bonus',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name=dashboard.models.Level),
            preserve_default=False,
        ),
    ]
