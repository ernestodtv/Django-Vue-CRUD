# Generated by Django 2.2.4 on 2019-08-28 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_note_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='attachment',
            field=models.FileField(upload_to=''),
        ),
    ]
