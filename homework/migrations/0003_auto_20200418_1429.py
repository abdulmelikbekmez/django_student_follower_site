# Generated by Django 3.0.5 on 2020-04-18 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_auto_20200418_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='email',
        ),
        migrations.RemoveField(
            model_name='homework',
            name='phone_number',
        ),
    ]