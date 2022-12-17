
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name= "index"),
    path('friend/<str:pk>', detail, name= "detail"),
    path('sent_msg/<str:pk>',sentMessages,name='sent_msg'),
    path('rcv_msg/<str:pk>',receivedMessages,name='rcv_msg'),
    
]