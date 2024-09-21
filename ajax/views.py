from django.shortcuts import render
from django.http import *
from customer.models import *
from owner.models import *
from django.template.loader import *
# Create your views here.
def bill_award(request):
    if request.method == 'GET':
        item_name = request.GET['item'].upper()
        item = Item.objects.filter(item_name=item_name).first()
        bill_id = request.GET['bill_id']
        bill = Bill.objects.filter(id=bill_id).first()
        if bill.drow_status == 1:
            Winner(
                bill_id=bill_id,
                item_id=item.id,
                amount=bill.amount
            ).save()
            bill.drow_status = 0
            bill.status = 0
            bill.save()
            winner = Winner.objects.filter(bill_id=bill_id,item_id=item.id).first()
        context={
            'winner':winner
        }
        t = render_to_string('ajax/customer/bill_award.html', context)
    return JsonResponse({'t': t})

def item_list(request):
    if request.method == 'GET':
        i = Item.objects.values().all()
        item = list(i)
    return JsonResponse({'t': item})

def size_edit(request):
    if request.method == 'GET':
        id = request.GET['id']
        size_input = request.GET['size_input']
        if id:
            if size_input:
                i = Item.objects.get(id=id)
                if size_input != i.size:
                    i.size = size_input
                    i.save()

    return JsonResponse({'t': 't'})