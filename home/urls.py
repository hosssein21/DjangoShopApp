from django.urls import path
from home import views

app_name='home'
urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('testimonial/',views.testimonial,name='testimonial'),
    
]
