# Generated by Django 3.1.1 on 2020-09-28 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='filename',
            new_name='name',
        ),
    ]
