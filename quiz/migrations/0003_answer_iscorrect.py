# Generated by Django 5.1.3 on 2024-12-14 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_answer_question_alter_question_topic_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='isCorrect',
            field=models.BooleanField(default=False),
        ),
    ]
