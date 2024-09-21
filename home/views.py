from django.shortcuts import render, redirect
from django.contrib import messages 
from owner.models import *
# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def test(request):
    item = Item.objects.all()
    
    context={
        'item':item
    }
    return render(request, 'home/test.html', context)

def login(request):
    if request.session.has_key('owner_mobile'):
        return redirect('/customer/customer_home/')
    if 'Login' in request.POST:
        num = request.POST.get('number')
        pin = request.POST.get('pin')
        owner_login={'mobile':'1252','pin':'1252'}
        if owner_login["mobile"]==num and owner_login["pin"]==pin:
            request.session['owner_mobile'] = request.POST.get('number')
            return redirect('/customer/customer_home/')
        else:
            messages.warning(request,"please insert correct information or call more suport 9921856831")
    return render(request, 'home/login.html')