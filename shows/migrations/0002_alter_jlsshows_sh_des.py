# Generated by Django 4.2 on 2023-05-02 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jlsshows',
            name='sh_des',
            field=models.CharField(db_comment='Show description', max_length=200),
        ),
    ]
