# Generated by Django 2.0.1 on 2018-01-14 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('father_id', models.CharField(default=0, max_length=30)),
                ('generation', models.CharField(max_length=10)),
                ('line', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=5)),
                ('content', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
