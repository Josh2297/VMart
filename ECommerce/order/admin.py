from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display=('trxn_id','buyer')
    search_fields=("trxn_id",'date')
    list_filter=('date','payment_status','delivery_status')

admin.site.register(Order,OrderAdmin)