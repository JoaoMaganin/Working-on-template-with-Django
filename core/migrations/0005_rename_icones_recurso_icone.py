# Generated by Django 4.2.2 on 2023-06-20 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recurso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recurso',
            old_name='icones',
            new_name='icone',
        ),
    ]
