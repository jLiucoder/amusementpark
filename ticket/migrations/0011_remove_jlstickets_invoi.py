# Generated by Django 4.2 on 2023-05-06 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0010_remove_jlstickets_tk_dis2_alter_jlstickets_invoi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jlstickets',
            name='invoi',
        ),
    ]
