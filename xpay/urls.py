from  django.urls import path

from xpay import views

urlpatterns = [
    path('',views.merchant_login),
    path('register',views.merchant_register),
    path('dash',views.dashboard),
]