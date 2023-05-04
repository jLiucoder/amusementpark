from django.db import models

from cart.models import JlsInvoi
from visitor.models import JlsVisitors


# Create your models here.


class JlsParkings(models.Model):
    pk_id = models.AutoField(primary_key=True, db_comment='Unique parking ID')
    pk_lot = models.CharField('Section', max_length=1, db_comment='Lot identifier')
    pk_timein = models.DateTimeField('From', db_comment='Time into the lot of the current viehicle')
    pk_timeout = models.DateTimeField('To', db_comment='Time get out of the current vehicle')
    pk_fee = models.IntegerField(db_comment='Parking fee during the parked time', null=True)
    v = models.ForeignKey(JlsVisitors, models.DO_NOTHING)
    invoi = models.ForeignKey(JlsInvoi, models.DO_NOTHING, null=True)

    class Meta:
        db_table = 'jls_parkings'
