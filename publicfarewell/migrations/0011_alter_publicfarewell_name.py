# Generated by Django 4.2.7 on 2023-11-11 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicfarewell', '0010_publicfarewell_owner_alter_publicfarewell_hidden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicfarewell',
            name='name',
            field=models.CharField(blank=True, default='익명', max_length=10, null=True),
        ),
    ]
