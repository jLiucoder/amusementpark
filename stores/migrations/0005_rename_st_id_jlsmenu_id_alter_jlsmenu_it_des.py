# Generated by Django 4.2 on 2023-05-03 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_jlsmenu_it_link_alter_jlsstores_st_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jlsmenu',
            old_name='st_id',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='jlsmenu',
            name='it_des',
            field=models.CharField(db_comment='Menu item description. ', max_length=200),
        ),
    ]
