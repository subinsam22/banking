# Generated by Django 4.2.6 on 2023-10-30 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='user',
            new_name='application_user',
        ),
    ]
