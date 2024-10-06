# Generated by Django 5.1.1 on 2024-10-04 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_project_goal_project_project_need_and_more'),
        ('register', '0002_register_major_alter_register_college_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True, default='暂无', max_length=100, null=True, verbose_name='项目描述'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, verbose_name='项目名称'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_goal',
            field=models.CharField(blank=True, default='暂无', max_length=100, null=True, verbose_name='项目目标'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_need',
            field=models.CharField(blank=True, default='暂无', max_length=100, null=True, verbose_name='项目需求'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_num',
            field=models.SmallIntegerField(default=0, verbose_name='项目人数'),
        ),
        migrations.AlterField(
            model_name='project',
            name='register',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.register', verbose_name='项目负责人'),
        ),
    ]
