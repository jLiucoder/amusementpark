# Generated by Django 4.2 on 2023-05-03 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jlsstores',
            name='st_menu_item',
        ),
        migrations.AddField(
            model_name='jlsstores',
            name='st_link',
            field=models.CharField(db_comment='link for the image', default='baidu.com', max_length=200),
        ),
        migrations.CreateModel(
            name='JlsStMenu',
            fields=[
                ('it_id', models.AutoField(db_comment='Unique Menu item ID', primary_key=True, serialize=False)),
                ('it_name', models.CharField(db_comment='Item name', max_length=20)),
                ('it_des', models.CharField(db_comment='Menu item description. ', max_length=20)),
                ('it_uprice', models.SmallIntegerField(db_comment='Menu item unit price. ')),
                ('st_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='stores.jlsstores')),
            ],
        ),
    ]