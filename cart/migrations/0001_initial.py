# Generated by Django 4.2 on 2023-04-23 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JlsAttractions',
            fields=[
                ('att_id', models.SmallIntegerField(db_comment='Unique Attration ID', primary_key=True, serialize=False)),
                ('att_name', models.CharField(db_comment='name of the attraction', max_length=10)),
                ('att_type', models.CharField(db_comment='Attraction type can be roller coaster, water ride, dark ride, kid ride etc. ', max_length=15)),
                ('att_descrip', models.CharField(db_comment='Attraction descriptions', max_length=30)),
                ('att_capacity', models.IntegerField(db_comment='Attraction capacity')),
                ('att_minhei', models.SmallIntegerField(db_comment='Minimum height requirement for the attraction in Centimeters. ')),
                ('att_duration', models.IntegerField(db_comment='Attraction duration, unit in MIN')),
                ('att_locsec', models.CharField(db_comment='Location section for the attraction', max_length=1)),
                ('att_status', models.CharField(db_comment='status can be closed, open, under mantainence', max_length=20)),
            ],
            options={
                'db_table': 'jls_attractions',
            },
        ),
        migrations.CreateModel(
            name='JlsInvoi',
            fields=[
                ('invoi_id', models.IntegerField(db_comment='Unique Invoice ID', primary_key=True, serialize=False)),
                ('nvoi_date', models.DateTimeField(db_comment='Date for the corresponding invoice')),
                ('invoi_quant', models.DecimalField(db_comment='Amount for the invoice', decimal_places=2, max_digits=4)),
                ('invoi_amount', models.IntegerField(db_comment='Invoice amount (how much money). ')),
                ('invoi_type', models.CharField(db_comment='Invoice type. Type can be "Tickets, Shows, Stores, Parkings". ', max_length=20)),
            ],
            options={
                'db_table': 'jls_invoi',
            },
        ),
        migrations.CreateModel(
            name='JlsPay',
            fields=[
                ('pay_id', models.IntegerField(db_comment='Unique payment ID for the payment', primary_key=True, serialize=False)),
                ('pay_method', models.CharField(db_comment='Payment method,CASH,CREDIT,DEBIT', max_length=8)),
                ('pay_date', models.DateTimeField(db_comment='Payment date of the current payment')),
                ('pay_amount', models.DecimalField(db_comment='Payment amount of the current payment', decimal_places=2, max_digits=3)),
                ('invoi', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cart.jlsinvoi')),
            ],
            options={
                'db_table': 'jls_pay',
            },
        ),
        migrations.CreateModel(
            name='JlsShows',
            fields=[
                ('sh_id', models.SmallIntegerField(db_comment='Unique show ID', primary_key=True, serialize=False)),
                ('sh_name', models.CharField(db_comment='Show name', max_length=10)),
                ('sh_type', models.CharField(db_comment='Show type can be drama, musical, comedy, horror, adventure ', max_length=10)),
                ('sh_des', models.CharField(db_comment='Show description', max_length=30)),
                ('sh_stime', models.DateTimeField(db_comment='Starting time of the show')),
                ('sh_etime', models.DateTimeField(db_comment='Ending time of the show')),
                ('sh_wcacc', models.CharField(db_comment='If the show is wheelchair accessible', max_length=1)),
                ('sh_price', models.DecimalField(db_comment='Price for the show', decimal_places=2, max_digits=3)),
            ],
            options={
                'db_table': 'jls_shows',
            },
        ),
        migrations.CreateModel(
            name='JlsStMenu',
            fields=[
                ('it_id', models.SmallIntegerField(db_comment='Unique Menu item ID', primary_key=True, serialize=False)),
                ('it_name', models.CharField(db_comment='Item name', max_length=20)),
                ('it_des', models.CharField(db_comment='Menu item description. ', max_length=20)),
                ('it_uprice', models.SmallIntegerField(db_comment='Menu item unit price. ')),
            ],
            options={
                'db_table': 'jls_st_menu',
            },
        ),
        migrations.CreateModel(
            name='JlsStores',
            fields=[
                ('st_id', models.IntegerField(db_comment='Unique store ID', primary_key=True, serialize=False)),
                ('st_name', models.CharField(db_comment='Name of the store', max_length=10)),
                ('st_cat', models.CharField(db_comment='Store category. Category can be Food stall, Ice cream parlor, Restaurant, Gift Shop, Apparels ', max_length=15)),
            ],
            options={
                'db_table': 'jls_stores',
            },
        ),
        migrations.CreateModel(
            name='JlsTickets',
            fields=[
                ('tk_id', models.IntegerField(db_comment='Unique ticket ID', primary_key=True, serialize=False)),
                ('tk_method', models.CharField(db_comment='Ticket method, online OL or onsite OS', max_length=2)),
                ('tk_purdate', models.DateTimeField(db_comment='Purchase date of the ticket')),
                ('tk_vdate', models.DateTimeField(db_comment='Visit date of the ticket')),
                ('tk_price', models.SmallIntegerField(db_comment='Ticket Price of the ticket')),
                ('tk_discount', models.IntegerField(db_comment='Percentage off of the ticket')),
                ('invoi', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cart.jlsinvoi')),
            ],
            options={
                'db_table': 'jls_tickets',
            },
        ),
        migrations.CreateModel(
            name='JlsVisitors',
            fields=[
                ('v_id', models.IntegerField(db_comment='Unique Visitor ID', primary_key=True, serialize=False)),
                ('v_fname', models.CharField(db_comment="Visitor's firstname", max_length=10)),
                ('v_lname', models.CharField(db_comment="Visitor's lastname", max_length=10)),
                ('v_state', models.CharField(db_comment="Visitor's state address", max_length=2)),
                ('v_city', models.CharField(db_comment="Visitor's city address", max_length=10)),
                ('v_staddr', models.CharField(db_comment="Visitor's street address", max_length=20)),
                ('v_zip', models.CharField(db_comment="Visitor's zipcode. ", max_length=5)),
                ('v_email', models.CharField(db_comment="Visitor's Email", max_length=30)),
                ('v_phone', models.CharField(db_comment="Visitor's phone number", max_length=10)),
                ('v_dob', models.DateTimeField(db_comment='date of birth of the visitor')),
                ('v_date', models.DateTimeField(db_comment='Visiting date for the visitor')),
                ('v_type', models.CharField(db_comment='Visitor type, can be "Group, Individual, Member or School". ', max_length=12)),
            ],
            options={
                'db_table': 'jls_visitors',
            },
        ),
        migrations.CreateModel(
            name='JlsCard',
            fields=[
                ('pay', models.OneToOneField(db_comment='Unique payment ID for the payment', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='cart.jlspay')),
                ('crd_fname', models.CharField(db_comment='card holder firstname.. ', max_length=10)),
                ('crd_lname', models.CharField(db_comment='Card holder lastname ', max_length=10)),
                ('crd_num', models.CharField(db_comment='Card number ', max_length=16)),
                ('crd_edate', models.DateTimeField(db_comment='Experition date of the card ')),
                ('crd_cvv', models.CharField(db_comment='CVV of card', max_length=3)),
                ('crd_type', models.CharField(db_comment='Card type. C for credit, D for debit', max_length=1)),
            ],
            options={
                'db_table': 'jls_card',
            },
        ),
        migrations.CreateModel(
            name='JlsGroup',
            fields=[
                ('v', models.OneToOneField(db_comment='Unique Visitor ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='cart.jlsvisitors')),
                ('group_size', models.IntegerField(db_comment='Group size. ')),
            ],
            options={
                'db_table': 'jls_group',
            },
        ),
        migrations.CreateModel(
            name='JlsIndivi',
            fields=[
                ('v', models.OneToOneField(db_comment='Unique Visitor ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='cart.jlsvisitors')),
                ('gender', models.CharField(db_comment='Gender can be male, female,non-binary. ', max_length=20)),
                ('nationality', models.CharField(db_comment='Nationality of individual. ', max_length=20)),
            ],
            options={
                'db_table': 'jls_indivi',
            },
        ),
        migrations.CreateModel(
            name='JlsMember',
            fields=[
                ('v', models.OneToOneField(db_comment='Unique Visitor ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='cart.jlsvisitors')),
                ('mem_id', models.IntegerField(db_comment='Membership ID.')),
                ('mem_sdate', models.DateTimeField(db_comment='Membership start date. ')),
                ('mem_edate', models.DateTimeField(db_comment='Membership end date. ')),
            ],
            options={
                'db_table': 'jls_member',
            },
        ),
        migrations.CreateModel(
            name='JlsSchool',
            fields=[
                ('v', models.OneToOneField(db_comment='Unique Visitor ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='cart.jlsvisitors')),
                ('school_id', models.IntegerField(db_comment='School ID.')),
                ('school_name', models.CharField(db_comment='School name. ', max_length=20)),
            ],
            options={
                'db_table': 'jls_school',
            },
        ),
        migrations.CreateModel(
            name='JlsTkAt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('att', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cart.jlsattractions')),
                ('tk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cart.jlstickets')),
            ],
            options={
                'db_table': 'jls_tk_at',
            },
        ),
        migrations.AddField(
            model_name='jlstickets',
            name='v',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cart.jlsvisitors'),
        ),
        migrations.CreateModel(
            name='JlsSummary',
            fields=[
                ('v_id', models.IntegerField(db_comment='Visitor ID. ', primary_key=True, serialize=False)),
                ('v_date', models.DateTimeField(db_comment='Visiting date. ')),
                ('tk_id', models.IntegerField(db_comment='Ticket ID.')),
                ('tk_amount', models.IntegerField(db_comment='Ticket amount. ')),
                ('sh_id', models.IntegerField(db_comment='Show ID.')),
                ('sh_amount', models.IntegerField(db_comment='Show amount. ')),
                ('st_id', models.IntegerField(db_comment='Store ID.')),
                ('st_amount', models.IntegerField(db_comment='Store amount. ')),
                ('pk_id', models.IntegerField(db_comment='Parking ID.')),
                ('pk_amount', models.IntegerField(db_comment='Parking amount. ')),
            ],
            options={
                'db_table': 'jls_summary',
                'unique_together': {('v_id', 'v_date')},
            },
        ),
        migrations.CreateModel(
            name='JlsParkings',
            fields=[
                ('pk_id', models.IntegerField(db_comment='Unique parking ID', primary_key=True, serialize=False)),
                ('pk_lot', models.CharField(db_comment='Lot identifier', max_length=1)),
                ('pk_timein', models.DateTimeField(db_comment='Time into the lot of the current viehicle')),
                ('pk_timeout', models.DateTimeField(db_comment='Time get out of the current vehicle')),
                ('pk_fee', models.SmallIntegerField(db_comment='Parking fee during the parked time')),
                ('invoi', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cart.jlsinvoi')),
                ('v', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cart.jlsvisitors')),
            ],
            options={
                'db_table': 'jls_parkings',
            },
        ),
        migrations.CreateModel(
            name='JlsVsi',
            fields=[
                ('invoi', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='cart.jlsinvoi')),
                ('sh', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cart.jlsshows')),
                ('v', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cart.jlsvisitors')),
            ],
            options={
                'db_table': 'jls_vsi',
            },
        ),
        migrations.CreateModel(
            name='JlsOrder',
            fields=[
                ('order_id', models.BigIntegerField(db_comment='Order ID for store items. ', primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(db_comment='Order date fore stores. ')),
                ('order_quant', models.SmallIntegerField(db_comment='Invoice quant for stores. ')),
                ('invoi', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cart.jlsinvoi')),
                ('it', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cart.jlsstmenu')),
                ('st', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cart.jlsstores')),
                ('v', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cart.jlsvisitors')),
            ],
            options={
                'db_table': 'jls_order',
                'unique_together': {('order_id', 'v')},
            },
        ),
    ]