# Generated by Django 2.2.12 on 2022-11-20 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20221120_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='status',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
