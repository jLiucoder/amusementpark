# Generated by Django 4.2 on 2023-05-06 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0008_alter_jlsshows_sh_price_jlsvsi'),
    ]

    operations = [
        migrations.AddField(
            model_name='jlsvsi',
            name='vsi_quant',
            field=models.DecimalField(db_comment='quantity of the shows', decimal_places=2, default=10, max_digits=5),
            preserve_default=False,
        ),
    ]
