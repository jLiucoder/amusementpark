# Generated by Django 4.2 on 2023-05-01 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0004_alter_jlsvisitors_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='jlsvisitors',
            name='v_dob',
            field=models.DateField(db_comment='date of birth of the visitor', default='2000-01-05', verbose_name='Birthday'),
            preserve_default=False,
        ),
    ]
