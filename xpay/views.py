from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
from xpay.form import RegisterForm


def merchant_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        user = authenticate(username=username, password=passwd)
        if user is not None:
            login(request, user)
            return redirect(merchant_register)
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
            print(form)
            return redirect(merchant_login)
    return render(request,'register.html',{'form':form})

