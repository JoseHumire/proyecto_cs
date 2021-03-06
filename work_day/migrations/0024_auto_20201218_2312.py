# Generated by Django 3.1.2 on 2020-12-18 23:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('work_day', '0023_auto_20201209_1207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatroom',
            options={'verbose_name': 'Chat Room', 'verbose_name_plural': 'Chat Rooms'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Country', 'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='curriculum',
            options={'verbose_name': 'Curriculum', 'verbose_name_plural': 'Curriculums'},
        ),
        migrations.AlterModelOptions(
            name='employment',
            options={'verbose_name': 'Employment', 'verbose_name_plural': 'Employments'},
        ),
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name': 'Job', 'verbose_name_plural': 'Jobs'},
        ),
        migrations.AlterModelOptions(
            name='joboffer',
            options={'verbose_name': 'Job Offer', 'verbose_name_plural': 'Job Offers'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
        migrations.AlterModelOptions(
            name='profession',
            options={'verbose_name': 'Profession', 'verbose_name_plural': 'Professions'},
        ),
        migrations.AlterModelOptions(
            name='professional',
            options={'verbose_name': 'Professional', 'verbose_name_plural': 'Professionals'},
        ),
        migrations.AlterModelOptions(
            name='school',
            options={'verbose_name': 'School', 'verbose_name_plural': 'Schools'},
        ),
        migrations.AlterModelOptions(
            name='study',
            options={'verbose_name': 'Study', 'verbose_name_plural': 'Studies'},
        ),
        migrations.RemoveField(
            model_name='city',
            name='name',
        ),
        migrations.RemoveField(
            model_name='country',
            name='name',
        ),
        migrations.RemoveField(
            model_name='profession',
            name='description',
        ),
        migrations.RemoveField(
            model_name='profession',
            name='name',
        ),
        migrations.RemoveField(
            model_name='school',
            name='name',
        ),
        migrations.AlterField(
            model_name='country',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='employment',
            name='description',
            field=models.TextField(default='', max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='description',
            field=models.CharField(default='', max_length=100, verbose_name='Description'),
        ),
        migrations.CreateModel(
            name='SchoolTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='work_day.school')),
            ],
            options={
                'verbose_name': 'School Translation',
                'db_table': 'work_day_school_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProfessionTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.CharField(default='', max_length=100, verbose_name='Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='work_day.profession')),
            ],
            options={
                'verbose_name': 'Profession Translation',
                'db_table': 'work_day_profession_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CountryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='work_day.country')),
            ],
            options={
                'verbose_name': 'Country Translation',
                'db_table': 'work_day_country_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CityTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='work_day.city')),
            ],
            options={
                'verbose_name': 'City Translation',
                'db_table': 'work_day_city_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
