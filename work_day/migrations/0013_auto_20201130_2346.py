# Generated by Django 3.1.2 on 2020-11-30 23:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('work_day', '0012_auto_20201130_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='finish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 1, 23, 46, 7, 255993, tzinfo=utc)),
        ),
    ]
