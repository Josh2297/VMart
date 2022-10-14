from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .product_form import ProductForm
from .models import Product 
from django.contrib.auth.decorators import permission_required,login_required,user_passes_test
from django.core.exceptions import PermissionDenied
from datetime import datetime
from PIL import Image
from django.core.files.images import ImageFile
from django.views import View
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth import get_user_model
from django.conf import settings
import re;import os
from order.models import Order
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

def product_form_view(request,user_id=None):
    if user_id:
        instance=get_object_or_404(pk=user_id)
    else:
        instance={}
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            updated_form=form.save(commit=False)
            updated_form.creator=get_object_or_404(get_user_model(),pk=request.user.id)
            updated_form.save()
            if instance:
                messages.success(request,"Product Saved Successfully")
            else:
                messages.success(request,'Product Updated Successfully')
            return redirect('homepage')
        else:
            print('Form Validation Status: ',form.is_valid())
    else:
        form=ProductForm(instance=instance)
    return render(request,'product_upload.html',{'form':form,'form_title':"Product Upload"})

# @permission_required(perm="",login_url="/accounts/login/")
def product_upload_view(request):
    products=Product.objects
    # Fruits Products
    fruits_products=products.filter(product_category__icontains='fruits').filter(availability="yes")
    fruits_1=fruits_products[:10];fruits_2=fruits_products[11:20]
    # Yam Products
    yam_product=products.filter(product_category__icontains='yam').filter(availability="yes")
    # Rice Products
    rice_1=products.filter(product_category__icontains='rice').filter(availability="yes")

    #Context
    context={'fruits':{'fruits_1':fruits_1,'fruits_2':fruits_2,'fruits':fruits_products},'yam':yam_product,'Rice':{'rice_1':rice_1}}
    return render(request,'products.html',context)

# Search Items in Categories and Fields

def Search(request): 
    if request.GET.get('search'):
        search_item=request.GET.get('search').lower();search_split=re.split(r'[^a-zA-Z]+',search_item)
        if len(search_item)>2:
            search_item=search_item[:-2]
        else:
            search_item=search_item[:-1]
        items=Product.objects.filter(product_category__icontains=search_item) # Number 1 Search In Category
        items=items.union(items.filter(product_name__icontains=search_item))
        if len(search_split)>1:
            for search_term in search_split:
                items=items.union(items.filter(product_category__icontains=search_term[:-1]))
                items=items.union(items.filter(product_name__icontains=search_term[:-1]))
        context={'category':('Search Term :'+request.GET.get('search')),'product_category':set(items)}
        return render(request,'product_view_page.html',context)
    else:
        return redirect('Products')

def SearchManage(request): # This Handles Search for Manage
    print('Search Item')
    if request.GET.get('search'):
        print('Search Item')
        items=Product.objects.filter(creator__id=request.user.id)
        search_item=request.GET.get('search')[:-2].lower();search_split=re.split(r'[^a-zA-Z]+',search_item)
        items=items.filter(product_category__icontains=search_item) # Number 1 Search In Category
        items=items.union(items.filter(product_name__icontains=search_item))
        if len(search_split)>1:
            for search_term in search_split:
                items=items.union(items.filter(product_category__icontains=search_term))
                items=items.union(items.filter(product_name__icontains=search_term))
        context={'title':("Result for Search: "+request.GET.get('search')),'products':set(items)}
    return render(request,'manage_products.html',context)
    '''else:
        return redirect('products')'''
# A View to Query All Objects From a Specific Category and Render in Browser

class Product_Category_Page(ListView):
    template_name='product_view_page.html'
    context_object_name='product_category'
    def get_queryset(self):
        category=self.kwargs['category'].lower()
        queryset=Product.objects.filter(product_category__icontains=category)
        return queryset
    def get_context_data(self,**kwargs):
        context=super(Product_Category_Page,self).get_context_data(**kwargs)
        context['category']=self.kwargs['category'].upper()
        return context


class Product_CBV(PermissionRequiredMixin,CreateView):
    model=Product
    # fields=('product_name','description','product_category','price','qty','perishable','product_picture')
    #fields=("product_name",'description','product_category','price','qty','perishable','product_picture')
    form_class=ProductForm
    success_url='/products/'
    template_name='product_upload.html'
    form_title=''
    permission_required="products.add_product"

    def get_context_data(self,**kwargs):
        context=super(Product_CBV,self).get_context_data(**kwargs)
        context['form_title']=self.form_title
        return context
    def form_valid(self,form):
        form.save(commit=False)
        form.instance.creator=get_object_or_404(get_user_model(),pk=self.request.user.id)
        form.save()
        messages.success(self.request,'Product Saved Successfully')
        return super(Product_CBV,self).form_valid(form)
# Update Products Page

class Product_Update_CBV(PermissionRequiredMixin,UpdateView):
    model=Product
    # fields=("product_name",'description','product_category','price','qty','perishable','product_picture','availability')
    form_class=ProductForm
    # success_url='products/manage/'
    template_name='product_update.html'
    form_title=''
    permission_required=("products.add_product","products.change_product")
    def get_context_data(self,**kwargs):
        context=super(Product_Update_CBV,self).get_context_data(**kwargs)
        context['form_title']=self.form_title
        return context
    def form_valid(self,form):
        form.save(commit=False)
        form.instance.creator=get_object_or_404(get_user_model(),pk=self.request.user.id)
        form.save()
        messages.success(self.request,"Product Updated Successfully")
        # return super(Product_Update_CBV,self).form_valid(form)
        return redirect('manage_products',form.instance.creator.id)

class ManageProduct(PermissionRequiredMixin,ListView):
    model=Product
    paginate_by=10
    template_name='manage_products.html'
    context_object_name='products'
    title=''
    permission_required=("products.add_product","products.change_product")
    def get_queryset(self):
        user=self.kwargs['user_id']
        products=Product.objects.filter(creator__id=user)
        return products

    def get_context_data(self,**kwargs):
        context=super(ManageProduct,self).get_context_data(**kwargs)
        context['title']=self.title
        return context

class DeleteProductConfirm(DetailView):
    model=Product
    template_name='delete_products.html'
    context_object_name="product"
    

def DeleteProduct(request,pk=None):
    Product.objects.get(pk=pk).delete()
    return redirect('manage_products',request.user.id)

# Product Description

class ProductDescription(DetailView):
    model=Product
    template_name="product Description.html"
    context_object_name='product'

    def get_context_data(self,**kwargs):
        context=super(ProductDescription,self).get_context_Data(**kwargs)
        # Add Similar Categories
        category=self.kwargs['category'];category=Product.objects.filter(product_category=category)
        context['similar_products']=category
        # Hot Deals
        #Top Discounts
        # Recommended For You
        return context

