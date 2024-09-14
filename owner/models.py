from django.db import models

# Create your models here.
class Bill(models.Model):
    bill_number = models.CharField(max_length=100)
    amount = models.FloatField()
    drow_status = models.IntegerField(default=1)
    status = models.IntegerField(default=1)
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    status = models.IntegerField(default=1)