# Generated by Django 4.2 on 2023-05-04 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0009_alter_jlsvisitors_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jlsgroup',
            name='group_size',
            field=models.IntegerField(db_comment='Group size. ', default=1),
        ),
    ]
