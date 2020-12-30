# Generated by Django 3.0.4 on 2020-12-30 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_id', models.IntegerField()),
                ('response', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=250)),
                ('date_start', models.DateTimeField()),
                ('date_finish', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ExamLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.IntegerField(editable=False)),
                ('host', models.CharField(default='127.0.0.1', editable=False, max_length=25)),
                ('bind_key', models.CharField(editable=False, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentID', models.CharField(editable=False, max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('correct_choice', models.IntegerField()),
                ('choices', models.ManyToManyField(related_name='choices', to='exams.Choice')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct', models.IntegerField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Student')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exams.ExamLocation'),
        ),
        migrations.AddField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(to='exams.Question'),
        ),
        migrations.AddField(
            model_name='exam',
            name='students',
            field=models.ManyToManyField(through='exams.Grade', to='exams.Student'),
        ),
    ]
