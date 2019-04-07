# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barajas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carta',
            name='habilidad',
            field=models.CharField(default='exit', max_length=60),
            preserve_default=False,
        ),
    ]
