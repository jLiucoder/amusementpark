# Generated by Django 4.2 on 2023-05-03 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_remove_jlsinvoi_invoi_quant'),
        ('ticket', '0003_alter_jlstickets_tk_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jlstickets',
            name='invoi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cart.jlsinvoi'),
        ),
    ]