# Generated by Django 4.2 on 2023-05-03 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_rename_jlsstmenu_jlsmenu_alter_jlsstores_st_cat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jlsmenu',
            name='it_link',
            field=models.CharField(db_comment='link for the image', default='google.com', max_length=200),
        ),
        migrations.AlterField(
            model_name='jlsstores',
            name='st_link',
            field=models.CharField(db_comment='link for the image', default='google.com', max_length=200),
        ),
    ]
