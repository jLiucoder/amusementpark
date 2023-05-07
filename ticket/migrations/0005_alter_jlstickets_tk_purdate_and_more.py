# Generated by Django 4.2 on 2023-05-03 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_alter_jlstickets_invoi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jlstickets',
            name='tk_purdate',
            field=models.DateTimeField(db_comment='Purchase datetime of the ticket'),
        ),
        migrations.AlterField(
            model_name='jlstickets',
            name='tk_vdate',
            field=models.DateField(db_comment='Visit date of the ticket'),
        ),
    ]