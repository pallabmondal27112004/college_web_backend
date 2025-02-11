# Generated by Django 5.1.3 on 2024-12-18 05:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_assignment_sent_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentlist',
            name='assignment_file',
            field=models.FileField(blank=True, null=True, upload_to='media/assignmet_file/'),
        ),
        migrations.AddField(
            model_name='assignmentlist',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='sent_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 12, 18, 11, 21, 21, 994678), null=True),
        ),
    ]
