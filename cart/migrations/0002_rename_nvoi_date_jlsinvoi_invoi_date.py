# Generated by Django 4.2 on 2023-04-23 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jlsinvoi',
            old_name='nvoi_date',
            new_name='invoi_date',
        ),
    ]
