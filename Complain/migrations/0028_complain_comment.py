# Generated by Django 2.2.5 on 2020-10-06 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Complain', '0027_delete_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='comment',
            field=models.ManyToManyField(to='Complain.Comment'),
        ),
    ]