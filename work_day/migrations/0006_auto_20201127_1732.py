# Generated by Django 3.1.2 on 2020-11-27 22:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('work_day', '0005_auto_20201127_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='finish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 22, 32, 50, 728280, tzinfo=utc)),
        ),
    ]
