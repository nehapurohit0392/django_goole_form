# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-25 12:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GForms', '0004_question_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_answer',
            name='form_owner',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]