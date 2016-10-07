# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-05 04:38
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crowdsourcing', '0147_auto_20160919_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='StripeAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stripe_id', models.CharField(db_index=True, max_length=128)),
                ('keys', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('external_accounts', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('managed', models.BooleanField(default=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stripe_account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
