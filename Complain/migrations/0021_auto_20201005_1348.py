# Generated by Django 3.0.3 on 2020-10-05 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Verified_User', '0003_auto_20200929_1529'),
        ('Complain', '0020_auto_20201005_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='vote',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Complain.Vote'),
        ),
        migrations.AlterUniqueTogether(
            name='complain',
            unique_together={('vote', 'user')},
        ),
        migrations.RemoveField(
            model_name='complain',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='complain',
            name='downvote',
        ),
    ]
