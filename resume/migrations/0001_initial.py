# Generated by Django 5.1.1 on 2024-09-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='resumeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pin', models.IntegerField()),
                ('state', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('job_city', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile/image/')),
                ('my_file', models.FileField(blank=True, null=True, upload_to='profile/file/')),
            ],
        ),
    ]
