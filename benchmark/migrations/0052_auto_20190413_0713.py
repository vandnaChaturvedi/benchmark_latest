# Generated by Django 2.0.8 on 2019-04-13 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('benchmark', '0051_auto_20190413_0638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='evaluation_measure_1',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='evaluation_measure_2',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='evaluation_measure_3',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='evaluation_measure_4',
        ),
    ]
