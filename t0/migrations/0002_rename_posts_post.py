# Generated by Django 4.1.1 on 2022-12-25 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('t0', '0001_initial'),
    ]

    operations = [ #renaming the table for display purposes
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]
