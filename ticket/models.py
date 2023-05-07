from django.db import models
from cart.models import JlsInvoi
from visitor.models import JlsVisitors

# Create your models here.

class JlsTickets(models.Model):
    tk_id = models.AutoField(primary_key=True, db_comment='Unique ticket ID')
    tk_method = models.CharField(max_length=2, db_comment='Ticket method, online OL or onsite OS')
    tk_purdate = models.DateTimeField(db_comment='Purchase datetime of the ticket')
    tk_vdate = models.DateField(db_comment='Visit date of the ticket')
    tk_price = models.SmallIntegerField(db_comment='Ticket Price of the ticket')
    tk_discount = models.FloatField(db_comment='Percentage off of the ticket')
    invoi = models.ForeignKey(JlsInvoi, on_delete=models.CASCADE, null=True)
    v = models.ForeignKey(JlsVisitors, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'jls_tickets'
