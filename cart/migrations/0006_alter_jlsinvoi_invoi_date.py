# Generated by Django 4.2 on 2023-05-04 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_jlsinvoi_invoi_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jlsinvoi',
            name='invoi_date',
            field=models.DateField(db_comment='Date for the corresponding invoice'),
        ),
    ]
