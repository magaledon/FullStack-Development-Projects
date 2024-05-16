from django.urls import path,include
from . import views
from django.views.generic.base import TemplateView

urlpatterns=[
    path('home',views.home,name="home"),
    path('register',views.register,name="register")
]