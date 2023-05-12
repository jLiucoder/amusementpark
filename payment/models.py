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
    pay_id = models.AutoField(primary_key=True, db_comment='Unique payment ID for the payment')
    pay_method = models.CharField(max_length=8, db_comment='Payment method,CASH,CREDIT,DEBIT')
    pay_date = models.DateField(db_comment='Payment date of the current payment')
    pay_amount = models.DecimalField(max_digits=6, decimal_places=2, db_comment='Payment amount of the current payment')

    crd_fname = models.CharField('First name', max_length=10, db_comment='card holder firstname.. ')
    crd_lname = models.CharField('Last name', max_length=10, db_comment='Card holder lastname ')
    crd_num = models.CharField('Card number', max_length=16, db_comment='Card number ')
    crd_edate = models.DateField('Expiration date', db_comment='Experition date of the card ')
    crd_cvv = models.CharField('CVV', max_length=3, db_comment='CVV of card')

    invoi = models.ForeignKey(JlsInvoi, models.DO_NOTHING, null=True)

    class Meta:
        db_table = 'jls_pay'


class JlsSummary(models.Model):
    s_id = models.AutoField("summary pk", primary_key=True, db_comment='summary pk')
    v_id = models.IntegerField("Visitor ID",
                               db_comment='Visitor ID. ')  # The composite primary key (v_id, v_date) found, that is not supported. The first column is selected.
    v_date = models.DateField("Visiting date", db_comment='Visiting date. ')
    amount = models.IntegerField("Amount", db_comment='amount.')
    source = models.CharField("Source", max_length=10, db_comment='source')
    source_id = models.IntegerField("Source ID", db_comment='source ID.')

    class Meta:
        db_table = 'jls_summary'
        ordering = ("s_id", "v_id", "v_date", "amount", "source", "source_id")

    def __str__(self):
        return f"{self.s_id}, {self.v_id}, {self.v_date}, {self.amount}, {self.source}, {self.source_id}"
