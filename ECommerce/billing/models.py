from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from order.models import Order

# Create your models here.

class Billing(models.Model):
    txn_id=models.OneToOneField(Order,on_delete=models.CASCADE,primary_key=True,help_text='Transaction ID is the unique code that Can Be Used To Track the status of an Order')
    first_name=models.CharField(max_length=20,verbose_name='First Name')
    last_name=models.CharField(max_length=20,verbose_name='Last Name')
    phone_no=models.CharField(max_length=15,verbose_name='Phone Number')
    email=models.EmailField(null=True,blank=True)
    delivery_method_list=(('home_delivery','Home Delivery'),('pick_up_station','Pick Up Station'))
    delivery_method=models.CharField(choices=delivery_method_list,max_length=20,default='home_delivery',null=False,blank=False)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    address=models.CharField(max_length=50,verbose_name='Delivery Address',help_text='Enter Shipping Address')
    total=models.IntegerField(verbose_name='Total Sum',help_text='Total Sum is in Naira')
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True,blank=True)
