from django.urls import path
from .views import *
urlpatterns = [
    path('',login,name='login'),
    path('login',cklogin,name='cklogin'),

]