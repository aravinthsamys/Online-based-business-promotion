# Generated by Django 4.2.11 on 2024-05-19 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ican', '0014_alter_businessdata_town_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='businessdata',
            old_name='photocopy',
            new_name='image',
        ),
    ]