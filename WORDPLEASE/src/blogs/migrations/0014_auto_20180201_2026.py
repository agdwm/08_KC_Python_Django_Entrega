# Generated by Django 2.0.1 on 2018-02-01 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0013_auto_20180119_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='release_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
