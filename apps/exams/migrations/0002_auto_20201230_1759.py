# Generated by Django 3.0.4 on 2020-12-30 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examlocation',
            name='bind_key',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='examlocation',
            name='host',
            field=models.CharField(default='127.0.0.1', max_length=25),
        ),
        migrations.AlterField(
            model_name='examlocation',
            name='port',
            field=models.IntegerField(),
        ),
    ]
