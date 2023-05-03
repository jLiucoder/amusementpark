from django.db import models


# Create your models here.

class JlsShows(models.Model):
    sh_id = models.AutoField(primary_key=True, db_comment='Unique show ID')
    sh_name = models.CharField(max_length=30, db_comment='Show name')
    sh_type = models.CharField(max_length=30, db_comment='Show type can be drama, musical, comedy, horror, adventure ')
    sh_des = models.CharField(max_length=300, db_comment='Show description')
    sh_stime = models.DateTimeField(db_comment='Starting time of the show')
    sh_etime = models.DateTimeField(db_comment='Ending time of the show')
    sh_wcacc = models.CharField(max_length=1, db_comment='If the show is wheelchair accessible')
    sh_price = models.DecimalField(max_digits=3, decimal_places=2, db_comment='Price for the show')
    # Added
    sh_link = models.CharField(max_length=200, default="baidu.com", db_comment='link for the image')

    class Meta:
        db_table = 'jls_shows'
