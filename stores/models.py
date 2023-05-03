from django.db import models


# Create your models here.

class JlsStores(models.Model):
    st_id = models.AutoField(primary_key=True, db_comment='Unique store ID')
    st_name = models.CharField(max_length=10, db_comment='Name of the store')
    st_cat = models.CharField(max_length=15,
                              db_comment='Store category. Category can be Food stall, Ice cream parlor, Restaurant, '
                                         'Gift Shop, Apparels ')
    st_menu_item = models.CharField(max_length=30,
                                    db_comment="Menu item name, serves as a composite primary key with st_id")

    # st_item_des = models.CharField()

    class Meta:
        # constraints
        db_table = 'jls_stores'
