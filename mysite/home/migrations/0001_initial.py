# Generated by Django 2.0.1 on 2018-01-27 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseNum', models.CharField(max_length=20)),
                ('courseCode', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queueSize', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(max_length=30)),
                ('studentID', models.CharField(max_length=20)),
                ('studentIssue', models.CharField(max_length=200)),
                ('studentEmail', models.CharField(max_length=50)),
                ('studentPhone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taEmail', models.EmailField(max_length=20)),
                ('taCode', models.CharField(max_length=20)),
                ('taName', models.CharField(max_length=30)),
                ('currentStudent', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='queue',
            name='students',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='courseTAs',
            field=models.ManyToManyField(to='home.TA'),
        ),
        migrations.AddField(
            model_name='course',
            name='queue',
            field=models.ManyToManyField(to='home.Queue'),
        ),
    ]
