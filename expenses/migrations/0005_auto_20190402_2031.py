# Generated by Django 2.1.7 on 2019-04-02 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_auto_20190402_2027'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Tag',
        ),
    ]
    atomic = False
