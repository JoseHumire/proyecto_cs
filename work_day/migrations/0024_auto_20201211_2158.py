# Generated by Django 3.1.2 on 2020-12-11 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work_day', '0023_auto_20201209_1207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['creation_date']},
        ),
    ]
