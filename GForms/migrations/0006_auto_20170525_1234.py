# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-25 12:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GForms', '0005_question_answer_form_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question_answer',
            name='form_id',
        ),
        migrations.RemoveField(
            model_name='question_answer',
            name='form_owner',
        ),
        migrations.DeleteModel(
            name='question_answer',
        ),
    ]
