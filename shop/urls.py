from django.urls import path
from shop import views

app_name='shop'
urlpatterns = [
    path('',views.product,name='product'),
    path('product_detail/',views.product_detail,name='product_detail'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    
]
