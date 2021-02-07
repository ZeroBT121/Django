#!/usr/bin/env python  
# -*- encoding:utf-8 -*-  
# author: zy
# time: 2021/2/5 10:46 
# file: urls.py 
from django.urls import path

from . import views

urlpatterns = [
    path('orders/', views.listorders),
    path('customers/', views.listcustomers),
]