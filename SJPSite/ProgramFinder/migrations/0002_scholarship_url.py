# Generated by Django 2.0.5 on 2018-05-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProgramFinder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='url',
            field=models.URLField(default='google'),
            preserve_default=False,
        ),
    ]
