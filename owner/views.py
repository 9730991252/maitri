from django.shortcuts import render, redirect
from django.contrib import messages 
from .models import *
# Create your views here.
def owner_login(request):
    if 'Login' in request.POST:
        num = request.POST.get('number')
        pin = request.POST.get('pin')
        owner_login={'mobile':'1252','pin':'1252'}
        if owner_login["mobile"]==num and owner_login["pin"]==pin:
            request.session['owner_mobile'] = request.POST.get('number')
            return redirect('/owner/owner_home/')
        else:
            messages.warning(request,"please insert correct information or call more suport 9921856831")
    return render(request, 'owner/owner_login.html')

def owner_home(request):
    if request.session.has_key('owner_mobile'):
        context={
            'item':Item.objects.all()
        }
        return render(request, 'owner/owner_home.html',context)
    else:
        return redirect('/login/')
    
def add_item(request):
    if request.session.has_key('owner_mobile'):
        if 'Add_iteml'in request.POST:
            item_name = request.POST.get('item_name').upper()
            size = request.POST.get('size')
            if Item.objects.filter(item_name=item_name).exists():
                messages.warning(request,"Item Allready Exits")
            else:
                Item(
                    item_name = item_name,
                    size=size,
                ).save()
                messages.success(request,"Item Added Success")
            return redirect('/owner/add_item/')
        context={
            'item':Item.objects.all()
        }
        return render(request, 'owner/add_item.html', context)
    else:
        return redirect('/login/')
    
def add_bill(request):
    if request.session.has_key('owner_mobile'):
        if 'add_new_bill'in request.POST:
            bill_number = request.POST.get('bill_number')
            amount = request.POST.get('bill_amount')
            if int(amount) < 1000:
                messages.warning(request,"Please Purchase More Than Rs. 1000  For Lucky Draw. Thank You ! ")
            else :
                if Bill.objects.filter(bill_number=bill_number).exists():
                    messages.warning(request,"Bill Alreday Exists. Thank You ! ")
                else:
                    Bill(
                        bill_number=bill_number,
                        amount=amount
                    ).save()
            return redirect('/owner/add_bill/')
        context={
            'bill':Bill.objects.filter(drow_status=1).order_by('-id')
        }
        return render(request, 'owner/add_bill.html',context)
    else:
        return redirect('/login/')
































