# Generated by Django 2.0.8 on 2019-05-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benchmark', '0062_auto_20190430_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='language',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='task',
            name='modality',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='task',
            name='purpose',
            field=models.CharField(default='', max_length=100),
        ),
    ]
