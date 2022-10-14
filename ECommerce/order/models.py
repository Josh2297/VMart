from django.db import models
from django.contrib.auth import get_user_model
from .transaction_id import random_generator
# Create your models here.

class Order(models.Model):
    trxn_id=models.CharField(verbose_name='Transaction ID',max_length=70,primary_key=True,default=random_generator())
    date=models.DateTimeField(verbose_name="Date of Order")
    order=models.CharField(max_length=10000,verbose_name='Order Items')
    total=models.IntegerField(verbose_name='Total of Purchase',help_text="Total of Goods Purchased Without Any Charges")
    amt_payable=models.IntegerField(help_text="Amount to be payed with Charges Included",null=True,blank=True)
    buyer=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True,blank=True)
    payment_status_list=(('pending','Pending'),('not_payed','Not Payed'),('failed','Failed'),('successful','Successful'))
    delivery_status_list=(('pending','Pending'),('delivered','Delivered'),('not_delivered','Not Delivered'),('delivery_failed','Delivery Failed'),('other','Other'))
    payment_status=models.CharField(choices=payment_status_list,max_length=20,default='pending',null=False,blank=False)
    delivery_status=models.CharField(choices=delivery_status_list,max_length=20,default='pending',null=False,blank=False)
    payment_id=models.CharField(max_length=10,null=True,blank=True)
    first_six_digit=models.IntegerField(null=True,blank=True)
    last_four_digit=models.IntegerField(null=True,blank=True)
    charged_amount=models.CharField(max_length=20,null=True,blank=True)
    payment_method=models.CharField(max_length=20,null=True,blank=True)
    payment_date=models.DateTimeField(verbose_name='Date and Time of Payment',null=True,blank=True)


    def __str__(self):
        return self.trxn_id