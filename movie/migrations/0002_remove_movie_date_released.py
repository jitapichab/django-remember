# Generated by Django 3.2.12 on 2022-04-02 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='date_released',
        ),
    ]
