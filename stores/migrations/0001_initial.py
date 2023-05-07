# Generated by Django 4.2 on 2023-05-02 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JlsStores',
            fields=[
                ('st_id', models.AutoField(db_comment='Unique store ID', primary_key=True, serialize=False)),
                ('st_name', models.CharField(db_comment='Name of the store', max_length=10)),
                ('st_cat', models.CharField(db_comment='Store category. Category can be Food stall, Ice cream parlor, Restaurant, Gift Shop, Apparels ', max_length=15)),
                ('st_menu_item', models.CharField(db_comment='Menu item name, serves as a composite primary key with st_id', max_length=30)),
            ],
            options={
                'db_table': 'jls_stores',
            },
        ),
    ]