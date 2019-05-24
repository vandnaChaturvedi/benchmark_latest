# Generated by Django 2.0.8 on 2018-09-26 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('benchmark', '0014_auto_20180926_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcategory',
            name='language',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='benchmark.Language'),
        ),
        migrations.AlterField(
            model_name='taskcategory',
            name='modality',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='benchmark.Modality'),
        ),
        migrations.AlterField(
            model_name='taskcategory',
            name='task',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='benchmark.Task'),
        ),
    ]
