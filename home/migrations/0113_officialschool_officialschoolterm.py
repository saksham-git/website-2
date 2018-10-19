# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-19 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0112_roundpage_lateprojects'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficialSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(help_text='University or college name', max_length=100)),
                ('university_website', models.URLField(help_text='University or college website')),
            ],
        ),
        migrations.CreateModel(
            name='OfficialSchoolTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_name', models.CharField(help_text='If the university uses term names (e.g. Winter 2018 term of Sophomore year), enter the current term name, year in college, and term year. If the university uses term numbers (e.g. 7th semester), enter the term number.', max_length=100, verbose_name='Term name or term number')),
                ('academic_calendar', models.URLField(blank=True, help_text='If necessary, save a file to a cloud hosting service and add the link to it here.', verbose_name='Link to the official academic calendar for this school term')),
                ('start_date', models.DateField(help_text='What is the first possible day of classes for all students?<br>If students who are in different school years or different semester numbers start classes on different dates, use the first possible date that students in that year or semester start classes.<br>If you do not know when the term will start, use the start date of that term from last year.', verbose_name='Date classes start. Use YYYY-MM-DD format.')),
                ('end_date', models.DateField(help_text='This is the date the university advertises for the last possible date of any exam for any student in the semester.', verbose_name='Date all exams end. Use YYYY-MM-DD format.')),
                ('typical_credits', models.IntegerField(blank=True, help_text='How many credits does a typical student register for?<br> If the university has different credit requirements for each semester for students in each major, pick the most common major listed by students in this university.', null=True, verbose_name='Number of credits for a typical student')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.OfficialSchool')),
            ],
        ),
    ]
