# Generated by Django 4.2 on 2023-05-12 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0016_alter_jlstickets_invoi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jlstickets',
            name='tk_purdate',
            field=models.DateField(db_comment='Purchase datetime of the ticket'),
        ),
    ]