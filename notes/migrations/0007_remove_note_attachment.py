# Generated by Django 2.2.4 on 2019-08-28 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20190828_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='attachment',
        ),
    ]