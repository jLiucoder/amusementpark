from django.db import models
from cart.models import JlsInvoi
# Create your models here.

# class JlsInvoi(models.Model):
#     invoi_id = models.IntegerField(primary_key=True, db_comment='Unique Invoice ID')
#     invoi_date = models.DateTimeField(db_comment='Date for the corresponding invoice')
#     invoi_quant = models.DecimalField(max_digits=4, decimal_places=2, db_comment='Amount for the invoice')
#     invoi_amount = models.IntegerField(db_comment='Invoice amount (how much money). ')
#     invoi_type = models.CharField(max_length=20, db_comment='Invoice type. Type can be "Tickets, Shows, Stores, Parkings". ')

#     class Meta:

#         db_table = 'jls_invoi'

class JlsPay(models.Model):
    pay_id = models.IntegerField(primary_key=True, db_comment='Unique payment ID for the payment')
    pay_method = models.CharField(max_length=8, db_comment='Payment method,CASH,CREDIT,DEBIT')
    pay_date = models.DateTimeField(db_comment='Payment date of the current payment')
    pay_amount = models.DecimalField(max_digits=3, decimal_places=2, db_comment='Payment amount of the current payment')
    invoi = models.ForeignKey(JlsInvoi, models.DO_NOTHING)

    class Meta:

        db_table = 'jls_pay'