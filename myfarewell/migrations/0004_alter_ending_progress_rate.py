# Generated by Django 4.2.7 on 2023-11-10 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfarewell', '0003_ending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ending',
            name='progress_rate',
            field=models.IntegerField(default=0),
        ),
    ]
