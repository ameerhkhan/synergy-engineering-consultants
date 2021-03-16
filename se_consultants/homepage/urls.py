from django.urls import path

# from homepage import views
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('message_sent/', views.message_sent, name='message_sent'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
]
