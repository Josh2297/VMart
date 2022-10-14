from django.shortcuts import render,redirect,get_object_or_404
from .billing_forms import BillingForm
from django.contrib import messages
from django.conf import settings 
from order.models import Order # Import Order Model
from User.models import CustomUser
import requests
from django.conf import settings
# Create your views here.

def Billings(request,txrn_id):
    txn_id=txrn_id
    order_model=get_object_or_404(Order,pk=txn_id)
    initial={'txn_id':order_model,'total':order_model.total,'total_amount':order_model.total}
    if request.user.is_authenticated:
        user_id=get_object_or_404(CustomUser,pk=request.user.id)
        initial['first_name']=user_id.first_name;initial['last_name']=user_id.last_name;initial['email']=user_id.email;\
        initial['phone_no']=user_id.phone_no
    if request.method=='POST':
        form=BillingForm(request.POST,initial=initial)
        if form.is_valid():
            print('Valid')
            updated_form=form.save(commit=False)
            updated_form.txn_id=order_model
            updated_form.total=order_model.amt_payable
            if request.user.is_authenticated:
                updated_form.user=user_id # Save User If User is Authenticated
            updated_form.save()
            # FlutterWave API Calls Trials
            response = requests.post("https://api.flutterwave.com/v3/payments",headers={'Authorization': "Bearer "+settings.FLUTTER_KEY},\
        json={'tx_ref': txn_id,'amount': updated_form.total,'currency': "NGN",'redirect_url': request.build_absolute_uri("/orders/checkout/payment/page/"),'customer': {'email': updated_form.email,'phonenumber': updated_form.phone_no,\
                'name': (updated_form.first_name+' '+updated_form.last_name)},'customizations':{'title': "VMart Tech Payments",'logo': request.build_absolute_uri("/static/food.jpg")\
            }})
            return redirect(response.json()['data']['link'])
    else:
        form=BillingForm(initial=initial)
    return render(request,'billing_form.html',{'form':form,'form_title':'Billing Form','transaction_id':txn_id,'total':order_model.total})