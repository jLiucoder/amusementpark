from django.db import models


# Create your models here.

class JlsAttractions(models.Model):
    att_id = models.AutoField(primary_key=True, db_comment='Unique Attration ID')
    att_name = models.CharField(max_length=20, db_comment='name of the attraction')
    att_type = models.CharField(max_length=20,
                                db_comment='Attraction type can be roller coaster, water ride, dark ride, kid ride '
                                           'etc. ')
    att_descrip = models.CharField(max_length=300, db_comment='Attraction descriptions')
    att_capacity = models.IntegerField(db_comment='Attraction capacity')
    att_minhei = models.SmallIntegerField(db_comment='Minimum height requirement for the attraction in Centimeters. ')
    att_duration = models.IntegerField(db_comment='Attraction duration, unit in MIN')
    att_locsec = models.CharField(max_length=1, db_comment='Location section for the attraction')
    att_status = models.CharField(max_length=20, db_comment='status can be closed, open, under mantainence')
    # Added
    att_link = models.CharField(max_length=200, default="baidu.com", db_comment='link for the image')

    class Meta:
        db_table = 'jls_attractions'
