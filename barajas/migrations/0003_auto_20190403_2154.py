# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barajas', '0002_carta_habilidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carta',
            name='habilidad',
            field=models.CharField(max_length=200),
        ),
    ]
