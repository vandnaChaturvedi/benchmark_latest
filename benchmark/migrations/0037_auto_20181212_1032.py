# Generated by Django 2.0.8 on 2018-12-12 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('benchmark', '0036_auto_20181211_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='task_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dataset', to='benchmark.TaskCategory'),
        ),
    ]
