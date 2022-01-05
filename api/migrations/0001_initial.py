# Generated by Django 4.0.1 on 2022-01-05 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(default='', max_length=8, unique=True)),
                ('host', models.CharField(max_length=30, unique=True)),
                ('guest_can_pause', models.BooleanField(default=False)),
                ('votes_to_skip', models.IntegerField(default=1)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
