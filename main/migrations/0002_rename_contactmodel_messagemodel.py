# Generated by Django 4.0.5 on 2022-07-02 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactModel',
            new_name='MessageModel',
        ),
    ]