# Generated by Django 2.0.8 on 2018-12-28 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('benchmark', '0039_auto_20181212_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groundtruth',
            name='task_category',
        ),
        migrations.RemoveField(
            model_name='groundtruthrow',
            name='ground_truth',
        ),
        migrations.RemoveField(
            model_name='resultrow',
            name='submission',
        ),
        migrations.DeleteModel(
            name='GroundTruth',
        ),
        migrations.DeleteModel(
            name='GroundTruthRow',
        ),
        migrations.DeleteModel(
            name='ResultRow',
        ),
    ]
