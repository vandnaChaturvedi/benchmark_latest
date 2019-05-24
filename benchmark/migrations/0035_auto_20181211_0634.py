# Generated by Django 2.0.8 on 2018-12-11 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('benchmark', '0034_auto_20181211_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='dataset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='submission', to='benchmark.Dataset'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='task_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission', to='benchmark.TaskCategory'),
        ),
    ]
