# Generated by Django 4.2.7 on 2023-11-07 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfarewell', '0002_remove_question_available_after_answer_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='theme',
            field=models.CharField(default='', max_length=200),
        ),
    ]
