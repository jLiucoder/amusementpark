from django.db import models


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


