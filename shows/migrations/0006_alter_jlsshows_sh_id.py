# Generated by Django 4.2 on 2023-05-02 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0005_alter_jlsshows_sh_des_alter_jlsshows_sh_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jlsshows',
            name='sh_id',
            field=models.AutoField(db_comment='Unique show ID', primary_key=True, serialize=False),
        ),
    ]