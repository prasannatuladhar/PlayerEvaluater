# Generated by Django 2.0 on 2018-08-30 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0003_auto_20180829_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='player3',
            field=models.CharField(default='Player3', max_length=25),
        ),
        migrations.AddField(
            model_name='player',
            name='player4',
            field=models.CharField(default='Player4', max_length=25),
        ),
        migrations.AddField(
            model_name='player',
            name='player5',
            field=models.CharField(default='Player5', max_length=25),
        ),
        migrations.AlterField(
            model_name='player',
            name='player1',
            field=models.CharField(default='Player1', max_length=25),
        ),
        migrations.AlterField(
            model_name='player',
            name='player2',
            field=models.CharField(default='Player2', max_length=25),
        ),
    ]
