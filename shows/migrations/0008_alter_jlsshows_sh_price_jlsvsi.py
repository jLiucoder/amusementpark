# Generated by Django 4.2 on 2023-05-06 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0010_alter_jlsgroup_group_size'),
        ('cart', '0006_alter_jlsinvoi_invoi_date'),
        ('shows', '0007_jlsshows_sh_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jlsshows',
            name='sh_price',
            field=models.DecimalField(db_comment='Price for the show', decimal_places=2, max_digits=5),
        ),
        migrations.CreateModel(
            name='JlsVsi',
            fields=[
                ('vsi_id', models.AutoField(db_comment='unique vsi id', primary_key=True, serialize=False)),
                ('invoi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.jlsinvoi')),
                ('sh', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shows.jlsshows')),
                ('v', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='visitor.jlsvisitors')),
            ],
            options={
                'db_table': 'jls_vsi',
            },
        ),
    ]
