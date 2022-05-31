# Generated by Django 4.0.4 on 2022-05-28 15:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0006_alter_project_bast_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='bast_value',
            field=models.IntegerField(max_length=3, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
