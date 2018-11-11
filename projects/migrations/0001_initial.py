# Generated by Django 2.0.4 on 2018-11-11 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Devtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('level', models.CharField(blank=True, max_length=200, null=True)),
                ('concept', models.CharField(blank=True, max_length=200, null=True)),
                ('projectimage1', models.CharField(blank=True, max_length=200, null=True)),
                ('projectimage2', models.CharField(blank=True, max_length=200, null=True)),
                ('projectimage3', models.CharField(blank=True, max_length=200, null=True)),
                ('requirement1', models.CharField(blank=True, max_length=200, null=True)),
                ('requirement2', models.CharField(blank=True, max_length=200, null=True)),
                ('requirement3', models.CharField(blank=True, max_length=200, null=True)),
                ('requirement4', models.CharField(blank=True, max_length=200, null=True)),
                ('requirement5', models.CharField(blank=True, max_length=200, null=True)),
                ('devtype', models.ForeignKey(null=True, on_delete=False, to='projects.Devtype')),
                ('framework', models.ForeignKey(null=True, on_delete=False, to='projects.Framework')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Projecttype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='projecttype',
            field=models.ForeignKey(null=True, on_delete=False, to='projects.Projecttype'),
        ),
        migrations.AddField(
            model_name='framework',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects.Language'),
        ),
    ]
