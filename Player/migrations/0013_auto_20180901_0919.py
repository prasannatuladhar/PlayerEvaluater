# Generated by Django 2.0 on 2018-09-01 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0012_auto_20180901_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='awayteam',
            field=models.TextField(default='awayteam', max_length=25),
        ),
        migrations.AddField(
            model_name='player',
            name='hometeam',
            field=models.TextField(default='hometeam', max_length=25),
        ),
    ]
