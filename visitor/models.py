from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class JlsVisitors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    v_id = models.AutoField(primary_key=True, db_comment='Unique Visitor ID')
    v_fname = models.CharField(max_length=10, db_comment="Visitor's firstname")
    v_lname = models.CharField(max_length=10, db_comment="Visitor's lastname")
    v_state = models.CharField(max_length=2, db_comment="Visitor's state address")
    v_city = models.CharField(max_length=10, db_comment="Visitor's city address")
    v_staddr = models.CharField(max_length=20, db_comment="Visitor's street address")
    v_zip = models.CharField(max_length=5, db_comment="Visitor's zipcode. ")
    v_email = models.CharField(max_length=30, db_comment="Visitor's Email")
    v_phone = models.CharField(max_length=10, db_comment="Visitor's phone number")
    # v_dob = models.DateTimeField(db_comment='date of birth of the visitor')
    # v_type = models.CharField(max_length=12, db_comment='Visitor type, can be "Group, Individual, Member or School". ')

    class Meta:
        # managed = False
        db_table = 'jls_visitors'
