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
from . import views
from django.views.generic import TemplateView

urlpatterns = [path('upload/',views.Product_CBV.as_view(form_title='Product_Upload'),name="product_upload"),\
    path('update/<int:pk>/',views.Product_Update_CBV.as_view(form_title='Product_Update'),name="product_update"),\
    path('',views.product_upload_view,name='products'),\
    path('categories/<str:category>/',views.Product_Category_Page.as_view(),name='products_view'),\
    path('search/',views.Search,name='search'),\
    path('manage/<str:user_id>/',views.ManageProduct.as_view(title="Your Products"),name="manage_products"),\
    path('confirm/delete/<str:pk>/',views.DeleteProductConfirm.as_view(),name="delete_product_confirm"),\
    path('delete/<str:pk>/',views.DeleteProduct,name="delete_product"),\
    path('search/manage/',views.SearchManage,name="search_manage"), # Search Products in Manager\
    path('description/<str:category>/<str:pk>/',views.ProductDescription.as_view(),name="product_description")
    ]

"{% url 'manage_products' user.id %}"