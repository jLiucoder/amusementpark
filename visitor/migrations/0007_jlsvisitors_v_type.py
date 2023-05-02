# Generated by Django 4.2 on 2023-05-01 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0006_alter_jlsmember_mem_edate_alter_jlsmember_mem_sdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='jlsvisitors',
            name='v_type',
            field=models.CharField(db_comment='Visitor type, can be "Group, Individual, Member', default='I', max_length=12),
        ),
    ]
