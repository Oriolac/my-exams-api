# Generated by Django 3.0.4 on 2021-01-07 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_auto_20210107_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='studentID',
            field=models.CharField(max_length=25),
        ),
    ]