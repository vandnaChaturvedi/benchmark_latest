# Generated by Django 2.0.8 on 2018-09-22 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benchmark', '0004_resource'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(default='', max_length=400)),
            ],
        ),
        migrations.AlterField(
            model_name='dataset',
            name='download_link',
            field=models.CharField(default='javascript:void(0);', max_length=100),
        ),
    ]
