# Generated by Django 3.2.9 on 2021-11-13 03:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211110_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='boat',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
