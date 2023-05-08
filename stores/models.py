from django.db import models

from cart.models import JlsInvoi
from visitor.models import JlsVisitors

# Create your models here.

class JlsStores(models.Model):
    st_id = models.AutoField(primary_key=True, db_comment='Unique store ID')
    st_name = models.CharField(max_length=50, db_comment='Name of the store')
    st_cat = models.CharField(max_length=40,
                              db_comment='Store category. Category can be Food stall, Ice cream parlor, Restaurant, '
                                         'Gift Shop, Apparels ')
    st_link = models.CharField(max_length=200, default="google.com", db_comment='link for the image')

    class Meta:
        # constraints
        db_table = 'jls_stores'


class JlsItems(models.Model):
    it_id = models.AutoField(primary_key=True, db_comment='Unique Menu item ID')
    it_name = models.CharField(max_length=20, db_comment='Item name')
    it_des = models.CharField(max_length=200, db_comment='Menu item description. ')
    it_uprice = models.SmallIntegerField(db_comment='Menu item unit price. ')
    it_link = models.CharField(max_length=200, default="google.com", db_comment='link for the image')
    # Foreign key
    st = models.ForeignKey(JlsStores, models.DO_NOTHING, null=True)
    class Meta:
        # constraints
        managed = True
        db_table = 'jls_items'


class JlsOrder(models.Model):
    order_id = models.AutoField(primary_key=True, db_comment='Order ID for store items.')  # The composite primary key (order_id, v_id) found, that is not supported. The first column is selected.
    order_date = models.DateTimeField(db_comment='Order date fore stores. ')
    order_quant = models.SmallIntegerField(db_comment='Invoice quant for stores. ')
    v = models.ForeignKey(JlsVisitors, models.DO_NOTHING)
    st = models.ForeignKey(JlsStores, models.DO_NOTHING)
    it = models.ForeignKey(JlsItems, models.DO_NOTHING)
    invoi = models.ForeignKey(JlsInvoi, models.CASCADE, null=True)

    class Meta:
        managed = True
        db_table = 'jls_order'
        # unique_together = (('order_id', 'v'),)