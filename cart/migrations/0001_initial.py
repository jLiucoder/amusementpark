# Generated by Django 4.2 on 2023-04-25 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JlsInvoi',
            fields=[
                ('invoi_id', models.IntegerField(db_comment='Unique Invoice ID', primary_key=True, serialize=False)),
                ('invoi_date', models.DateTimeField(db_comment='Date for the corresponding invoice')),
                ('invoi_quant', models.DecimalField(db_comment='Amount for the invoice', decimal_places=2, max_digits=4)),
                ('invoi_amount', models.IntegerField(db_comment='Invoice amount (how much money). ')),
                ('invoi_type', models.CharField(db_comment='Invoice type. Type can be "Tickets, Shows, Stores, Parkings". ', max_length=20)),
            ],
            options={
                'db_table': 'jls_invoi',
            },
        ),
    ]
