# Generated by Django 4.0.4 on 2022-04-21 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0003_linkproject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='female',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='male',
        ),
    ]
