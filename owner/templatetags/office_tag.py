from django import template
from customer.models import *
from datetime import timedelta, date
register = template.Library()

@register.simple_tag
def Award_List(id):
    qty = Winner.objects.filter(item_id=id).count()
    return qty
