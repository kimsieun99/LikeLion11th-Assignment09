# Generated by Django 4.2.2 on 2023-06-22 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diarynotform',
            name='image',
            field=models.ImageField(blank=True, upload_to='phto/'),
        ),
    ]