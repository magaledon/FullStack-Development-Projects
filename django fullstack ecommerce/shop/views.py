from django.shortcuts import render
from django.urls import path


def home(request):
    return render(request,'shop1/index.html')
def register(request):
    return render(request,'shop1/register.html')