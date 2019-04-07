# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barajas', '0004_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='Edicion',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
