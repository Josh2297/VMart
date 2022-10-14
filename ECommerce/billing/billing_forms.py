from django import forms
from .models import Billing


class BillingForm(forms.ModelForm):
    class Meta:
        model=Billing
        exclude=('user','txn_id','total')
        widgets={# 'txn_id':forms.TextInput(attrs={'disabled':True}),
        'delivery_method':forms.RadioSelect,
        }

    total_amount=forms.IntegerField(min_value=0,required=False,label='Total Amount to Pay',help_text='Total Amount is in Naira',widget=forms.NumberInput(attrs={'disabled':True}))
    
    consent=forms.BooleanField(label="Do You Consent to Our Terms And Condition",required=True,initial=True)
