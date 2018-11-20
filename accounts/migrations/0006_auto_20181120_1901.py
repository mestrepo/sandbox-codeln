# Generated by Django 2.0.4 on 2018-11-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_availabilty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='core',
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d'),
        ),
    ]
