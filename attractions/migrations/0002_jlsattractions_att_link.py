# Generated by Django 4.2 on 2023-05-02 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jlsattractions',
            name='att_link',
            field=models.CharField(db_comment='link for the image', default='baidu.com', max_length=200),
        ),
    ]
