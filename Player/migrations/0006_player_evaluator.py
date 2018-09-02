# Generated by Django 2.0 on 2018-08-31 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Player', '0005_remove_player_block_counter_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='evaluator',
            field=models.ForeignKey(default='Evaluator', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
