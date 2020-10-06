# Generated by Django 2.2.5 on 2020-10-06 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Verified_User', '0003_auto_20200929_1529'),
        ('Complain', '0028_complain_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Verified_User.Verified_User'),
        ),
    ]
