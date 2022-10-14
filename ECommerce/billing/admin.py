from django.contrib import admin
from .models import Billing

class BillingAdmin(admin.ModelAdmin):
    list_display=('txn_id','email','user')
    search_fields=('txn_id','email')
    list_filter=('city','state')

admin.site.register(Billing,BillingAdmin)
# Register your models here.
