# Generated by Django 2.1 on 2020-07-25 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0003_auto_20200725_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]