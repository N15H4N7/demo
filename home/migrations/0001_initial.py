# Generated by Django 3.0.7 on 2021-03-20 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YrBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=0)),
                ('branch', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=10, unique=True)),
                ('subject_name', models.CharField(default='', max_length=100)),
                ('visibilty', models.BooleanField(default=True)),
                ('yr_branch', models.ManyToManyField(to='home.YrBranch')),
            ],
        ),
    ]
