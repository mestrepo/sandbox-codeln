# Generated by Django 2.0.4 on 2018-11-23 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatesprojects',
            name='candidate',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
