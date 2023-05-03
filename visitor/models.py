from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class JlsVisitors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    v_id = models.AutoField(primary_key=True, db_comment='Unique Visitor ID')
    v_fname = models.CharField('Firstname', max_length=10, db_comment="Visitor's firstname")
    v_lname = models.CharField('Lastname', max_length=10, db_comment="Visitor's lastname")
    v_state = models.CharField('State', max_length=2, db_comment="Visitor's state address")
    v_city = models.CharField('City', max_length=10, db_comment="Visitor's city address")
    v_staddr = models.CharField('Street', max_length=20, db_comment="Visitor's street address")
    v_zip = models.CharField('ZIP', max_length=5, db_comment="Visitor's zipcode. ")
    v_email = models.CharField('Email', max_length=30, db_comment="Visitor's Email")
    v_phone = models.CharField('Phone', max_length=10, db_comment="Visitor's phone number")
    v_dob = models.DateField('Birthday', db_comment='date of birth of the visitor')
    v_type = models.CharField(max_length=12, default='I', db_comment='Visitor type, can be "Group, Individual, Member')
    v_group = models.CharField(max_length=1, default='N', db_comment='if user is in a group')

    class Meta:
        # managed = False
        db_table = 'jls_visitors'


class JlsMember(models.Model):
    v = models.OneToOneField('JlsVisitors', models.DO_NOTHING, primary_key=True, db_comment='Unique Visitor ID')
    mem_id = models.IntegerField(db_comment='Membership ID.')
    mem_sdate = models.DateField(db_comment='Membership start date. ')
    mem_edate = models.DateField(db_comment='Membership end date. ')

    class Meta:
        db_table = 'jls_member'


class JlsGroup(models.Model):
    v = models.OneToOneField('JlsVisitors', models.DO_NOTHING, primary_key=True, db_comment='Unique Visitor ID')
    group_size = models.IntegerField(default=0, db_comment='Group size. ')

    class Meta:

        db_table = 'jls_group'
