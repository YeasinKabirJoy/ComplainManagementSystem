# Generated by Django 3.0.3 on 2020-10-05 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Verified_User', '0003_auto_20200929_1529'),
        ('Complain', '0022_auto_20201005_1550'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='complain',
            unique_together={('user', 'upvote', 'downvote')},
        ),
    ]
