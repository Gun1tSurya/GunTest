# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total_quantity', models.IntegerField(default=0)),
                ('total_amount', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('line_total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('invoice_id', models.ForeignKey(related_name='transactions', to='CRUD.Invoice')),
            ],
        ),
    ]
