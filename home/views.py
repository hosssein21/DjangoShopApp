from django.shortcuts import render

def index(request):
    return render(request,'home/index.html')

def contact(request):
    return render(request,'home/contact.html')

def testimonial(request):
    return render(request,'home/testimonial.html')