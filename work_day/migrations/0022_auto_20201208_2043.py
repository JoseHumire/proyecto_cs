# Generated by Django 3.1.2 on 2020-12-09 01:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('work_day', '0021_auto_20201208_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='job',
            name='finish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 10, 1, 43, 25, 149024, tzinfo=utc)),
        ),
    ]
