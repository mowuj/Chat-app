
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name= "index"),
    path('friend/<str:pk>', detail, name= "detail"),
    
]