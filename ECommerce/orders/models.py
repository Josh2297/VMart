from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Orders(models.Model):
    trxn_id=models.CharField(verbose_name='Transaction ID',max_length=20,primary_key=True)
    date=models.DateField(verbose_name="Date of Order",auto_now=True)
    order=models.CharField(max_length=10000,verbose_name='Order Items')
    total=models.IntegerField(verbose_name='Total of Purchase')
    buyer=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.trxn_id