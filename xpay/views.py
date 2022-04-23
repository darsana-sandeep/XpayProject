from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from xpay.form import RegisterForm
from xpay.models import Merchant


def merchant_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        user = authenticate(username=username, password=passwd)
        if user is not None:
            login(request, user)
            return redirect(dashboard)
        else:

            return redirect(merchant_login)
            return HttpResponse('<h1>invalid username or password</h1>')
    return render(request, 'login.html')

def merchant_register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            # business = request.POST['business']
            # phone = request.POST['phone']
            # city = request.POST['city']
            # busi = request.POST['busi']
            # location = request.POST['location']
            # website = request.POST['website']
            # member = Merchant.objects.create(business=business,phone=phone, city=city, busi=busi, location=location,website=website)
            # member.save()
            return redirect(dashboard)

        else:

            return redirect(merchant_login)
    return render(request,'register.html',{'form':form})

def dashboard(request):
    return render(request,'home.html')




