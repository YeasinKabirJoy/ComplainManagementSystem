# Generated by Django 2.2.5 on 2020-10-07 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Complain', '0033_auto_20201007_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
