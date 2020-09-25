# Generated by Django 3.1.1 on 2020-09-24 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_code', models.CharField(max_length=100000000000000000000)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.author')),
            ],
        ),
    ]
