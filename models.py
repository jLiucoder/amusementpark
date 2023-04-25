from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# all models are here to copy and paste

#
# class JlsAttractions(models.Model):
#     att_id = models.SmallIntegerField(primary_key=True, db_comment='Unique Attration ID')
#     att_name = models.CharField(max_length=10, db_comment='name of the attraction')
#     att_type = models.CharField(max_length=15, db_comment='Attraction type can be roller coaster, water ride, dark ride, kid ride etc. ')
#     att_descrip = models.CharField(max_length=30, db_comment='Attraction descriptions')
#     att_capacity = models.IntegerField(db_comment='Attraction capacity')
#     att_minhei = models.SmallIntegerField(db_comment='Minimum height requirement for the attraction in Centimeters. ')
#     att_duration = models.IntegerField(db_comment='Attraction duration, unit in MIN')
#     att_locsec = models.CharField(max_length=1, db_comment='Location section for the attraction')
#     att_status = models.CharField(max_length=20, db_comment='status can be closed, open, under mantainence')
#
#     class Meta:
#
#         db_table = 'jls_attractions'
#
#
# class JlsCard(models.Model):
#     pay = models.OneToOneField('JlsPay', models.DO_NOTHING, primary_key=True, db_comment='Unique payment ID for the payment')
#     crd_fname = models.CharField(max_length=10, db_comment='card holder firstname.. ')
#     crd_lname = models.CharField(max_length=10, db_comment='Card holder lastname ')
#     crd_num = models.CharField(max_length=16, db_comment='Card number ')
#     crd_edate = models.DateTimeField(db_comment='Experition date of the card ')
#     crd_cvv = models.CharField(max_length=3, db_comment='CVV of card')
#     crd_type = models.CharField(max_length=1, db_comment='Card type. C for credit, D for debit')
#
#     class Meta:
#
#         db_table = 'jls_card'
#
#
# class JlsGroup(models.Model):
#     v = models.OneToOneField('JlsVisitors', models.DO_NOTHING, primary_key=True, db_comment='Unique Visitor ID')
#     group_size = models.IntegerField(db_comment='Group size. ')
#
#     class Meta:
#
#         db_table = 'jls_group'
#
#
# class JlsIndivi(models.Model):
#     v = models.OneToOneField('JlsVisitors', models.DO_NOTHING, primary_key=True, db_comment='Unique Visitor ID')
#     gender = models.CharField(max_length=20, db_comment='Gender can be male, female,non-binary. ')
#     nationality = models.CharField(max_length=20, db_comment='Nationality of individual. ')
#
#     class Meta:
#
#         db_table = 'jls_indivi'

#
# class JlsInvoi(models.Model):
#     invoi_id = models.IntegerField(primary_key=True, db_comment='Unique Invoice ID')
#     invoi_date = models.DateTimeField(db_comment='Date for the corresponding invoice')
#     invoi_quant = models.DecimalField(max_digits=4, decimal_places=2, db_comment='Amount for the invoice')
#     invoi_amount = models.IntegerField(db_comment='Invoice amount (how much money). ')
#     invoi_type = models.CharField(max_length=20, db_comment='Invoice type. Type can be "Tickets, Shows, Stores, Parkings". ')
#
#     class Meta:
#
#         db_table = 'jls_invoi'
#

# class JlsMember(models.Model):
#     v = models.OneToOneField('JlsVisitors', models.DO_NOTHING, primary_key=True, db_comment='Unique Visitor ID')
#     mem_id = models.IntegerField(db_comment='Membership ID.')
#     mem_sdate = models.DateTimeField(db_comment='Membership start date. ')
#     mem_edate = models.DateTimeField(db_comment='Membership end date. ')
#
#     class Meta:
#
#         db_table = 'jls_member'
#
#
# class JlsOrder(models.Model):
#     order_id = models.BigIntegerField(primary_key=True, db_comment='Order ID for store items. ')  # The composite primary key (order_id, v_id) found, that is not supported. The first column is selected.
#     order_date = models.DateTimeField(db_comment='Order date fore stores. ')
#     order_quant = models.SmallIntegerField(db_comment='Invoice quant for stores. ')
#     v = models.ForeignKey('JlsVisitors', models.DO_NOTHING)
#     st = models.ForeignKey('JlsStores', models.DO_NOTHING)
#     it = models.ForeignKey('JlsStMenu', models.DO_NOTHING)
#     invoi = models.ForeignKey(JlsInvoi, models.DO_NOTHING)
#
#     class Meta:
#
#         db_table = 'jls_order'
#         unique_together = (('order_id', 'v'),)
#
#
# class JlsParkings(models.Model):
#     pk_id = models.IntegerField(primary_key=True, db_comment='Unique parking ID')
#     pk_lot = models.CharField(max_length=1, db_comment='Lot identifier')
#     pk_timein = models.DateTimeField(db_comment='Time into the lot of the current viehicle')
#     pk_timeout = models.DateTimeField(db_comment='Time get out of the current vehicle')
#     pk_fee = models.SmallIntegerField(db_comment='Parking fee during the parked time')
#     v = models.ForeignKey('JlsVisitors', models.DO_NOTHING)
#     invoi = models.ForeignKey(JlsInvoi, models.DO_NOTHING)
#
#     class Meta:
#
#         db_table = 'jls_parkings'
#
#
# class JlsPay(models.Model):
#     pay_id = models.IntegerField(primary_key=True, db_comment='Unique payment ID for the payment')
#     pay_method = models.CharField(max_length=8, db_comment='Payment method,CASH,CREDIT,DEBIT')
#     pay_date = models.DateTimeField(db_comment='Payment date of the current payment')
#     pay_amount = models.DecimalField(max_digits=3, decimal_places=2, db_comment='Payment amount of the current payment')
#     invoi = models.ForeignKey(JlsInvoi, models.DO_NOTHING)
#
#     class Meta:
#
#         db_table = 'jls_pay'
#
#
# class JlsSchool(models.Model):
#     v = models.OneToOneField('JlsVisitors', models.DO_NOTHING, primary_key=True, db_comment='Unique Visitor ID')
#     school_id = models.IntegerField(db_comment='School ID.')
#     school_name = models.CharField(max_length=20, db_comment='School name. ')
#
#     class Meta:
#
#         db_table = 'jls_school'
#
#
# class JlsShows(models.Model):
#     sh_id = models.SmallIntegerField(primary_key=True, db_comment='Unique show ID')
#     sh_name = models.CharField(max_length=10, db_comment='Show name')
#     sh_type = models.CharField(max_length=10, db_comment='Show type can be drama, musical, comedy, horror, adventure ')
#     sh_des = models.CharField(max_length=30, db_comment='Show description')
#     sh_stime = models.DateTimeField(db_comment='Starting time of the show')
#     sh_etime = models.DateTimeField(db_comment='Ending time of the show')
#     sh_wcacc = models.CharField(max_length=1, db_comment='If the show is wheelchair accessible')
#     sh_price = models.DecimalField(max_digits=3, decimal_places=2, db_comment='Price for the show')
#
#     class Meta:
#
#         db_table = 'jls_shows'
#
#
# class JlsStMenu(models.Model):
#     it_id = models.SmallIntegerField(primary_key=True, db_comment='Unique Menu item ID')
#     it_name = models.CharField(max_length=20, db_comment='Item name')
#     it_des = models.CharField(max_length=20, db_comment='Menu item description. ')
#     it_uprice = models.SmallIntegerField(db_comment='Menu item unit price. ')
#
#     class Meta:
#
#         db_table = 'jls_st_menu'
#
#
# class JlsStores(models.Model):
#     st_id = models.IntegerField(primary_key=True, db_comment='Unique store ID')
#     st_name = models.CharField(max_length=10, db_comment='Name of the store')
#     st_cat = models.CharField(max_length=15, db_comment='Store category. Category can be Food stall, Ice cream parlor, Restaurant, Gift Shop, Apparels ')
#
#     class Meta:
#
#         db_table = 'jls_stores'
#
#
# class JlsSummary(models.Model):
#     v_id = models.IntegerField(primary_key=True, db_comment='Visitor ID. ')  # The composite primary key (v_id, v_date) found, that is not supported. The first column is selected.
#     v_date = models.DateTimeField(db_comment='Visiting date. ')
#     tk_id = models.IntegerField(db_comment='Ticket ID.')
#     tk_amount = models.IntegerField(db_comment='Ticket amount. ')
#     sh_id = models.IntegerField(db_comment='Show ID.')
#     sh_amount = models.IntegerField(db_comment='Show amount. ')
#     st_id = models.IntegerField(db_comment='Store ID.')
#     st_amount = models.IntegerField(db_comment='Store amount. ')
#     pk_id = models.IntegerField(db_comment='Parking ID.')
#     pk_amount = models.IntegerField(db_comment='Parking amount. ')
#
#     class Meta:
#
#         db_table = 'jls_summary'
#         unique_together = (('v_id', 'v_date'),)
#
#
# class JlsTickets(models.Model):
#     tk_id = models.IntegerField(primary_key=True, db_comment='Unique ticket ID')
#     tk_method = models.CharField(max_length=2, db_comment='Ticket method, online OL or onsite OS')
#     tk_purdate = models.DateTimeField(db_comment='Purchase date of the ticket')
#     tk_vdate = models.DateTimeField(db_comment='Visit date of the ticket')
#     tk_price = models.SmallIntegerField(db_comment='Ticket Price of the ticket')
#     tk_discount = models.IntegerField(db_comment='Percentage off of the ticket')
#     v = models.ForeignKey('JlsVisitors', models.DO_NOTHING)
#     invoi = models.ForeignKey(JlsInvoi, models.DO_NOTHING)
#
#     class Meta:
#
#         db_table = 'jls_tickets'
#
#
# class JlsTkAt(models.Model):
#     tk = models.ForeignKey(JlsTickets, models.DO_NOTHING)
#     att = models.ForeignKey(JlsAttractions, models.DO_NOTHING)
#
#     class Meta:
#
#         db_table = 'jls_tk_at'
#
#
# # class JlsVisitors(models.Model):
# #     v_id = models.IntegerField(primary_key=True, db_comment='Unique Visitor ID')
# #     v_fname = models.CharField(max_length=10, db_comment="Visitor's firstname")
# #     v_lname = models.CharField(max_length=10, db_comment="Visitor's lastname")
# #     v_state = models.CharField(max_length=2, db_comment="Visitor's state address")
# #     v_city = models.CharField(max_length=10, db_comment="Visitor's city address")
# #     v_staddr = models.CharField(max_length=20, db_comment="Visitor's street address")
# #     v_zip = models.CharField(max_length=5, db_comment="Visitor's zipcode. ")
# #     v_email = models.CharField(max_length=30, db_comment="Visitor's Email")
# #     v_phone = models.CharField(max_length=10, db_comment="Visitor's phone number")
# #     v_dob = models.DateTimeField(db_comment='date of birth of the visitor')
# #     v_date = models.DateTimeField(db_comment='Visiting date for the visitor')
# #     v_type = models.CharField(max_length=12, db_comment='Visitor type, can be "Group, Individual, Member or School". ')
# #
# #     class Meta:
# #
# #         db_table = 'jls_visitors'
#
#
# class JlsVsi(models.Model):
#     v = models.ForeignKey(JlsVisitors, models.DO_NOTHING)
#     sh = models.ForeignKey(JlsShows, models.DO_NOTHING)
#     invoi = models.OneToOneField(JlsInvoi, models.DO_NOTHING, primary_key=True)
#
#     class Meta:
#
#         db_table = 'jls_vsi'
