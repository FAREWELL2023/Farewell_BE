# Generated by Django 4.2.7 on 2023-11-11 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicfarewell', '0012_alter_publicfarewell_name_alter_questions_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicFarewell2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=300)),
                ('content', models.TextField(max_length=300)),
            ],
        ),
    ]
