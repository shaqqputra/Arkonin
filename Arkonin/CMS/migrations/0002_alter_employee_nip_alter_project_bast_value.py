# Generated by Django 4.0.4 on 2022-04-21 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='nip',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='bast_value',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
