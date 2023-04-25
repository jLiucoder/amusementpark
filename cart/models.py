from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class JlsInvoi(models.Model):
    invoi_id = models.IntegerField(primary_key=True, db_comment='Unique Invoice ID')
    invoi_date = models.DateTimeField(db_comment='Date for the corresponding invoice')
    invoi_quant = models.DecimalField(max_digits=4, decimal_places=2, db_comment='Amount for the invoice')
    invoi_amount = models.IntegerField(db_comment='Invoice amount (how much money). ')
    invoi_type = models.CharField(max_length=20,
                                  db_comment='Invoice type. Type can be "Tickets, Shows, Stores, Parkings". ')

    class Meta:
        db_table = 'jls_invoi'
