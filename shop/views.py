from django.shortcuts import render

def product(request):
    return render(request,'shop/shop.html')

def product_detail(request):
    return render(request,'shop/shop-detail.html')

def cart(request):
    return render(request,'shop/cart.html')

def checkout(request):
    return render(request,'shop/checkout.html')