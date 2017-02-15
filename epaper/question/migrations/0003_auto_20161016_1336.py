# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-16 13:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_courselevel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_title', models.CharField(max_length=250)),
                ('subject_medium', models.CharField(max_length=10)),
                ('subject_description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='courselevel',
            name='course_medium',
        ),
        migrations.AddField(
            model_name='subject',
            name='course_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.CourseLevel'),
        ),
    ]