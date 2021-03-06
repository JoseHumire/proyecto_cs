# Generated by Django 3.1.2 on 2020-12-08 19:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('work_day', '0018_merge_20201207_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='professional',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='work_day.country'),
        ),
        migrations.AlterField(
            model_name='employment',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employments', to='work_day.joboffer'),
        ),
        migrations.AlterField(
            model_name='job',
            name='cv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='work_day.curriculum'),
        ),
        migrations.AlterField(
            model_name='job',
            name='finish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 9, 19, 4, 37, 960536, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='job_offers', to='work_day.city'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_offers', to='work_day.professional'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='professionals', to='work_day.city'),
        ),
        migrations.AlterField(
            model_name='study',
            name='cv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studies', to='work_day.curriculum'),
        ),
    ]
