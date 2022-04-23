from  django.urls import path

from xpay import views

urlpatterns = [
    path('',views.merchant_login),
    path('register',views.merchant_register),
    path('logout',views.merchant_logout),
    path('dash',views.dashboard),
    path('add_product',views.add_product),
    path('list',views.list_product),
    path('delete/<int:id>',views.delete_product),
    path('edit/<int:id>', views.product_edit),
    path('edit/update/<int:id>', views.product_update)
]