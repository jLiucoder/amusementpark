# Generated by Django 4.2 on 2023-05-03 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0009_alter_jlsvisitors_user'),
        ('parking', '0003_alter_jlsparkings_v'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jlsparkings',
            name='v',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='visitor.jlsvisitors'),
        ),
    ]
