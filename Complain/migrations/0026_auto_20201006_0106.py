# Generated by Django 3.0.3 on 2020-10-05 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Complain', '0025_auto_20201005_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='complain',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='complain',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
