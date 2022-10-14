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
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from .views import Profile_Page
from django.contrib.auth import views
from products.views import product_upload_view

urlpatterns = [
    path("",product_upload_view,name='products'),\
    path('admin/',admin.site.urls),\
    path('allauth/',include('allauth.urls')),\
    path('accounts/',include(('django.contrib.auth.urls', 'auth'),namespace='accounts')),\
    path('customers/',include('customers.urls'),name='Customers'),\
    path('user/',include('User.urls'),name='Users'),\
    path('products/',include('products.urls'),name='Products'),\
    path('transactions/',include('transactions.urls'),name='Transactions'),\
    path('orders/',include('order.urls'),name='Orders'),\
    path('billing/',include('billing.urls'),name='billing'),\
    path('profile/',Profile_Page.as_view(),name='profile_page'),\
    path("reset/<uidb64>/<token>/",views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path("password_reset/done/",views.PasswordResetDoneView.as_view(),name="password_reset_done"),\
    path("reset/done/",views.PasswordResetCompleteView.as_view(),name="password_reset_complete")
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
