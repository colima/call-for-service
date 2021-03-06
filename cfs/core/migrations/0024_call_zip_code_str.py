# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_nature_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='zip_code_str',
            field=models.CharField(max_length=5, null=True, blank=True),
        ),
        migrations.RunSQL(
            """
            UPDATE call SET zip_code_str = z.descr FROM zip_code z
            WHERE call.zip_code_id = z.zip_code_id
            """
        )
    ]
