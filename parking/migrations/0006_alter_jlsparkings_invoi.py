# Generated by Django 4.2 on 2023-05-06 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_alter_jlsinvoi_invoi_date'),
        ('parking', '0005_alter_jlsparkings_pk_lot_alter_jlsparkings_pk_timein_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jlsparkings',
            name='invoi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.jlsinvoi'),
        ),
    ]