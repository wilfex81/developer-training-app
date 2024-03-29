# Generated by Django 4.0.4 on 2023-03-20 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='complexity',
            field=models.CharField(choices=[('Difficulty levels', (('easy', 'Easy'), ('medium', 'Intermediate'), ('hard', 'Hard')))], max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='modules',
            field=models.CharField(choices=[('Modules', (('module one', 'Module one'), ('module two', 'Module two'), ('module three', 'Module three')))], max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='tasks',
            field=models.CharField(choices=[('Tasks Assigned', (('Task one', 'Task one'), ('Task two', 'Task two'), ('Task three', 'Task three')))], max_length=100),
        ),
    ]
