# Generated by Django 2.0.5 on 2018-05-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('description', models.CharField(max_length=500)),
                ('deadlineMonth', models.PositiveSmallIntegerField()),
                ('deadlineDay', models.PositiveSmallIntegerField()),
                ('amount', models.PositiveIntegerField()),
                ('upperAmount', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]
