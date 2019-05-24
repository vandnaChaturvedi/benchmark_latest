# Generated by Django 2.0.8 on 2018-09-21 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benchmark', '0002_dataset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='download_link',
            field=models.CharField(default='javascipt:void(0);', max_length=100),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='short_text',
            field=models.CharField(default='', max_length=300),
        ),
    ]
