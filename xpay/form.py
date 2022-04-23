from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from xpay.models import Product


class RegisterForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')

class ProductForm(forms.ModelForm):
    class Meta():
        model = Product
        fields = '__all__'