# Generated by Django 2.1 on 2020-09-04 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventRestService', '0002_auto_20200904_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalmeetings',
            name='agenda',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
    ]
