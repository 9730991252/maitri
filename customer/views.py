from django.shortcuts import render, redirect
from owner.models import *
# Create your views here.
def customer_home(request):
    if request.session.has_key('owner_mobile'):
        context={
            'bills':Bill.objects.filter(drow_status=1)
        }
        return render(request, 'customer/customer_home.html', context)
    else:
        return redirect('/login/')
    
def lucky_draw(request, bill_id):
    if request.session.has_key('owner_mobile'):
        bill = Bill.objects.get(id=bill_id)
        if bill.drow_status == 1:
            context={
                'bill':bill
            }
        if bill.drow_status == 0:
            return redirect('/customer/customer_home/')
        return render(request, 'customer/lucky_draw.html', context)
    else:
        return redirect('/login/')