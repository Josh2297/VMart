from django.shortcuts import render,redirect
from django.http import JsonResponse
import json;from random import choice,shuffle
from .models import Order
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from ast import literal_eval
from billing.models import Billing
from django.views.generic import ListView,DetailView
import requests;import os
from ast import literal_eval
from .transaction_id import random_generator
from django.conf import settings

# Create your views here.

'''def Create_Txn_ID():
    # Generate Unique Transaction Id
    txn_id='TXN';number_range=[x for x in range(10)];
    letter_range=[chr(x) for x in range(65,91)];letter_range.extend([chr(x) for x in range(97,123)]) # List of alphabets
    for value in range(10):
        txn_id+=str((choice(number_range)))
    for value in range(7):
        txn_id+=str(choice(letter_range))
    shuf_part=list(txn_id[3:]);shuffle(shuf_part);shuf_part=''.join(shuf_part)
    txn_id=txn_id[:3]+shuf_part
    return txn_id'''

def OrderCall(request):
    txn_id=random_generator();order_model=Order()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data_post=json.load(request)['item_data'];total=0
        for d in data_post:
            total+=(int(d['price']))
        # Handling Saving Items to Order Model
        order_model.trxn_id=txn_id
        order_model.date=timezone.now()
        order_model.order=str(data_post)
        order_model.total=total
        if request.user.is_authenticated:
            order_model.buyer=get_object_or_404(get_user_model(),pk=request.user.id)
        order_model.save() # Save Model
        # print(data_post);print(type(data_post));
        return JsonResponse({'data':txn_id},status=200)

def OrderPage(request,trxn_id):
    txn_id=trxn_id;order_model=get_object_or_404(Order,pk=txn_id)
    orders=literal_eval(order_model.order);prod_total=order_model.total
    trans_cost=float(settings.TRANSPORTATION_COST) # Transportation Cost
    total=prod_total+trans_cost;payment_rate=(float(settings.TRANSACTION_RATE)/100)*prod_total;total=total+payment_rate
    order_model.amt_payable=total;order_model.save() # Save Amount Payable
    return render(request,'order_table.html',{'orders':orders,'transaction_id':txn_id,'total':total,'prod_total':prod_total,'trans_cost':trans_cost,'payment_rate':payment_rate})

def PaymentOrderPage(request):
    if request.GET.get('status') and request.GET.get('tx_ref'):
        txn_id=request.GET.get('tx_ref');order_model=get_object_or_404(Order,pk=txn_id);orders=literal_eval(order_model.order)
        payment_id=request.GET.get('transaction_id') # Get Payment ID
        status=request.GET.get('status')
        billing_model=get_object_or_404( Billing,pk=order_model)
        if request.GET.get('status')=='successful':
            " Get Order Model and Update Status to Successful"
            # Verify Transaction From Verify Transaction API
            url='https://api.flutterwave.com/v3/transactions/verify_by_reference'
            response=requests.get(url,headers={'Authorization': "Bearer "+settings.FLUTTER_KEY},params={'tx_ref':txn_id})
            if response.json() and response.json()['status']:
                order_model.payment_status=(response.json()['status']+'ful')
                order_model.payment_id=response.json()['data']['id']
                order_model.charged_amount=response.json()['data']['charged_amount']
                order_model.first_six_digit=response.json()['data']['card']['first_6digits']
                order_model.last_four_digit=response.json()['data']['card']['last_4digits']
                order_model.payment_date=response.json()['data']['customer']['created_at']
                order_model.save()
                return render(request,'payment_page.html',{'order_model':order_model,'orders':orders,'billing_model':billing_model,'status':(order_model.payment_status)})
        
            order_model.payment_status='pending';order_model.payment_id=payment_id
            return render(request,'payment_page.html',{'order_model':order_model,'orders':orders,'billing_model':billing_model,'status':'Pending'})
        
        else:
            order_model.payment_status='failed'
            order_model.payment_id=payment_id
            order_model.save()
            return render(request,'payment_page.html',{'order_model':order_model,'orders':orders,'billing_model':billing_model,'status':status})
    else: # If Status is Not Returned, Redirect to Homepage
        return redirect('/products/')

class OrderHistoryPage(DetailView):
    '''This Class Returns the Result of a seacrh for order History '''
    model=Order
    template_name='order_page.html'
    context_object_name='order'
    '''def get_queryset(self):
        order_model=get_object_or_404(Order,pk=self.kwargs['pk'])
        self.order_model=order_model
        return order_model'''
    def get_context_data(self,**kwargs):
        context=super(OrderHistoryPage,self).get_context_data(**kwargs)
        order_model=self.get_object()
        # Add Billing To Context
        billing=get_object_or_404(Billing,pk=order_model)
        context['billing']=billing
        # Add Orders To Context
        context['orders']=literal_eval(order_model.order)
        return context
