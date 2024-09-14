from django.db import models
from owner.models import *
# Create your models here.
class Winner(models.Model):
    bill = models.ForeignKey(Bill,on_delete=models.PROTECT,null=True,blank=True)
    item = models.ForeignKey(Item,on_delete=models.PROTECT,null=True,blank=True)
    amount = models.FloatField()
    date = models.DateField(auto_now_add=True, null=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True)
