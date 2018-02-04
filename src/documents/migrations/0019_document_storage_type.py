# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-04 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0018_auto_20170715_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='storage_type',
            field=models.CharField(choices=[('unencrypted', 'Unencrypted'), ('gpg', 'Encrypted with GNU Privacy Guard')], default='gpg', editable=False, max_length=11),
        ),
    ]