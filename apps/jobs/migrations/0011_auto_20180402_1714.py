# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-02 20:14
from __future__ import unicode_literals

from django.db import migrations
from django.utils.text import slugify


def create_slugify_jobs(apps, schema_editor):
    Jobs = apps.get_model('jobs.Job')

    for job in Jobs.objects.filter(slug=None):
        job.slug = slugify(job.titulo_do_job)
        job.save()


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_job_slug'),
    ]

    operations = [
        migrations.RunPython(create_slugify_jobs),
    ]
