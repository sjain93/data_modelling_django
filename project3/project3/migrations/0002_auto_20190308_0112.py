# Generated by Django 2.1.5 on 2019-03-08 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project3', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='critic',
            old_name='comapny',
            new_name='company',
        ),
    ]