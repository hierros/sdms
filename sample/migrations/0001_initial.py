# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AmountUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount_unit_name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feedstock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feedstock_name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fraction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fraction_name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('building', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sample_name', models.CharField(max_length=128)),
                ('comment', models.TextField(null=True, blank=True)),
                ('amount', models.IntegerField(null=True, blank=True)),
                ('external_id', models.CharField(max_length=128)),
                ('owner_name', models.CharField(max_length=128)),
                ('custodian_name', models.CharField(max_length=128)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('mod_date', models.DateField(auto_now_add=True)),
                ('trb_num', models.IntegerField(null=True, blank=True)),
                ('trb_page', models.IntegerField(null=True, blank=True)),
                ('specific_hazard', models.CharField(max_length=128, null=True, blank=True)),
                ('label_description', models.TextField(null=True, blank=True)),
                ('amount_unit', models.ForeignKey(blank=True, to='sample.AmountUnit', null=True)),
                ('feedstock', models.ForeignKey(blank=True, to='sample.Feedstock', null=True)),
                ('fraction', models.ForeignKey(blank=True, to='sample.Fraction', null=True)),
                ('location', models.ForeignKey(blank=True, to='sample.Location', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('treatment_name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sample',
            name='status',
            field=models.ForeignKey(blank=True, to='sample.Status', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sample',
            name='treatment',
            field=models.ForeignKey(blank=True, to='sample.Treatment', null=True),
            preserve_default=True,
        ),
    ]
