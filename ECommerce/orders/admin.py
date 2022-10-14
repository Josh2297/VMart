from django.contrib import admin
from .models import Orders
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display=('trxn_id','buyer')
    search_fields=("trxn_id",'date')
    list_filter=('buyer','date')

admin.site.register(Orders,OrderAdmin)