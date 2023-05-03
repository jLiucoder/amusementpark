from django.db import models
from cart.models import JlsInvoi
from visitor.models import JlsVisitors

# Create your models here.

class JlsTickets(models.Model):
    tk_id = models.AutoField(primary_key=True, db_comment='Unique ticket ID')
    tk_method = models.CharField(max_length=2, db_comment='Ticket method, online OL or onsite OS')
    tk_purdate = models.DateTimeField(db_comment='Purchase date of the ticket')
    tk_vdate = models.DateTimeField(db_comment='Visit date of the ticket')
    tk_price = models.SmallIntegerField(db_comment='Ticket Price of the ticket')
    tk_discount = models.IntegerField(db_comment='Percentage off of the ticket')
    v = models.ForeignKey(JlsVisitors, models.DO_NOTHING)
    invoi = models.ForeignKey(JlsInvoi, models.DO_NOTHING)

    class Meta:

        db_table = 'jls_tickets'