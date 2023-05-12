# Generated by Django 4.2 on 2023-05-12 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_jlssummary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jlssummary',
            options={'ordering': ('s_id', 'v_id', 'v_date', 'amount', 'source', 'source_id')},
        ),
        migrations.AlterField(
            model_name='jlssummary',
            name='amount',
            field=models.IntegerField(db_comment='amount.', verbose_name='Amount'),
        ),
        migrations.AlterField(
            model_name='jlssummary',
            name='s_id',
            field=models.AutoField(db_comment='summary pk', primary_key=True, serialize=False, verbose_name='summary pk'),
        ),
        migrations.AlterField(
            model_name='jlssummary',
            name='source',
            field=models.CharField(db_comment='source', max_length=10, verbose_name='Source'),
        ),
        migrations.AlterField(
            model_name='jlssummary',
            name='source_id',
            field=models.IntegerField(db_comment='source ID.', verbose_name='Source ID'),
        ),
        migrations.AlterField(
            model_name='jlssummary',
            name='v_date',
            field=models.DateField(db_comment='Visiting date. ', verbose_name='Visiting date'),
        ),
        migrations.AlterField(
            model_name='jlssummary',
            name='v_id',
            field=models.IntegerField(db_comment='Visitor ID. ', verbose_name='Visitor ID'),
        ),
    ]