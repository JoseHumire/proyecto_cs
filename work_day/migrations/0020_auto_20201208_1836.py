# Generated by Django 3.1.2 on 2020-12-08 23:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('work_day', '0019_auto_20201208_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='finish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 9, 23, 36, 44, 340220, tzinfo=utc)),
        ),
    ]
