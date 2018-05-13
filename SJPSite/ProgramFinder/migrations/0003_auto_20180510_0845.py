# Generated by Django 2.0.5 on 2018-05-10 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProgramFinder', '0002_scholarship_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholarship',
            name='deadline',
        ),
        migrations.AddField(
            model_name='scholarship',
            name='deadlineDay',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scholarship',
            name='deadlineMonth',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
