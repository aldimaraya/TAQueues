# Generated by Django 2.0.1 on 2018-01-27 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_queue_queuesize'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='queueSize',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
