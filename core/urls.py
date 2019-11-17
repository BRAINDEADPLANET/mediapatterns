from django.urls import path
from django.shortcuts import redirect
from .views import index
from .views import post_detail


urlpatterns = [
    path('', index),
    path('<str:slug>', post_detail, name='post_detail'),
]