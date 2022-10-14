"""ECommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views
from django.views.generic import TemplateView
from ECommerce.views import Profile_Page
urlpatterns = [path('ajax/',views.OrderCall,name="ajax"),\
                path('checkout/<str:trxn_id>/',views.OrderPage,name='order_page'),\
                    path('checkout/payment/page/',views.PaymentOrderPage,name='payment_page'),\
                path('list/',Profile_Page.as_view(template_name='order_list.html'),name='profile_list'),\
                path('order/<str:pk>/',views.OrderHistoryPage.as_view(),name='order_history'),\
                path('track/',TemplateView.as_view(template_name='track_order.html'),name='track_order')]