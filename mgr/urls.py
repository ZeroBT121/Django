#!/usr/bin/env python  
# -*- encoding:utf-8 -*-  
# author: zy
# time: 2021/2/5 10:46 
# file: urls.py 
from django.urls import path
from mgr import customers, sign_in_out

urlpatterns = [
    path('customers', customers.dispatcher),
    path('signin', sign_in_out.signin),
    path('signout', sign_in_out.signout),
]