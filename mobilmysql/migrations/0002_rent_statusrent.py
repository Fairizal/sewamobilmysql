# Generated by Django 3.1.4 on 2021-01-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobilmysql', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='statusRent',
            field=models.BooleanField(default=False),
        ),
    ]
