# Generated by Django 4.2.7 on 2023-11-07 12:55

from django.db import migrations, models
import publicfarewell.models


class Migration(migrations.Migration):

    dependencies = [
        ('publicfarewell', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicfarewell',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=publicfarewell.models.image_upload_path),
        ),
    ]
