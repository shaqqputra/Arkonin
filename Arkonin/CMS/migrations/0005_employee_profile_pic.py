# Generated by Django 4.0.4 on 2022-05-27 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0004_remove_employee_female_remove_employee_male'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to='images/profile/'),
        ),
    ]
