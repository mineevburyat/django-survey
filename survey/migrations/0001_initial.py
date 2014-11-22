# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AnswerInteger',
            fields=[
                ('answerbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='survey.AnswerBase')),
                ('body', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=('survey.answerbase',),
        ),
        migrations.CreateModel(
            name='AnswerRadio',
            fields=[
                ('answerbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='survey.AnswerBase')),
                ('body', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=('survey.answerbase',),
        ),
        migrations.CreateModel(
            name='AnswerSelect',
            fields=[
                ('answerbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='survey.AnswerBase')),
                ('body', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=('survey.answerbase',),
        ),
        migrations.CreateModel(
            name='AnswerSelectMultiple',
            fields=[
                ('answerbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='survey.AnswerBase')),
                ('body', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=('survey.answerbase',),
        ),
        migrations.CreateModel(
            name='AnswerText',
            fields=[
                ('answerbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='survey.AnswerBase')),
                ('body', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=('survey.answerbase',),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('required', models.BooleanField()),
                ('question_type', models.CharField(default=b'text', max_length=200, choices=[(b'text', b'text'), (b'radio', b'radio'), (b'select', b'select'), (b'select-multiple', b'Select Multiple'), (b'integer', b'integer')])),
                ('choices', models.TextField(help_text=b'if the question type is "radio," "select," or "select multiple" provide a comma-separated list of options for this question .', null=True, blank=True)),
                ('order', models.SmallIntegerField(default=0)),
                ('category', models.ForeignKey(blank=True, to='survey.Category', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('conditions', models.TextField(null=True, verbose_name=b'Conditions during interview', blank=True)),
                ('comments', models.TextField(null=True, verbose_name=b'Any additional Comments', blank=True)),
                ('interview_uuid', models.CharField(max_length=36, verbose_name=b'Interview unique identifier')),
                ('interviewee', models.ForeignKey(related_name='interviewee', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('interviewer', models.ForeignKey(related_name='interviewer', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='response',
            name='survey',
            field=models.ForeignKey(to='survey.Survey'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(to='survey.Survey'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='survey',
            field=models.ForeignKey(to='survey.Survey'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answerbase',
            name='question',
            field=models.ForeignKey(to='survey.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answerbase',
            name='response',
            field=models.ForeignKey(to='survey.Response'),
            preserve_default=True,
        ),
    ]
