from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect


# Create your views here.


from xpay.form import RegisterForm, ProductForm
from xpay.models import Merchant, Product


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
            return redirect(dashboard)

        else:

            return redirect(merchant_login)
    return render(request,'register.html',{'form':form})

def merchant_logout(request):
    logout(request)
    return redirect(merchant_login)
@login_required
def dashboard(request):
    return render(request,'home.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Getting the current instance object to display in the template
            img_object = form.instance

            return redirect(list_product)
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})


def list_product(request):

    list = Product.objects.all()
    return render(request,'list_product.html',{'list':list})

def delete_product(request,id):
    list = Product.objects.get(id=id)
    list.delete()
    return redirect(add_product)

def product_edit(request, id):

    members = Product.objects.get(id=id)
    return render(request, 'product_edit.html', {"members":members})

def product_update(request, id):
    member = Product.objects.get(id=id)
    member.product_name = request.POST['Product']
    member.category = request.POST['Category']
    member.brand = request.POST['Brand']
    member.price = request.POST['Price']
    member.gst = request.POST['GST']
    member.description = request.POST['product_description']
    member.save()
    return redirect(list_product)


def view_profile(request):
    current_user= request.user
    member = User.objects.get(id=current_user.id)
    return render(request,'view_profile.html',{'member':member})










