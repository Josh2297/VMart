from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from PIL import Image
from django.core.exceptions import ValidationError

# Create your models here.
# Product Table
class Product(models.Model):
    creator=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    product_name=models.CharField(max_length=50,null=False,blank=False)
    description=models.TextField(null=True,blank=True,verbose_name="Products Description",max_length=200)
    class Categories():
        product_categories=(('hot_deals','Hot Deals'),('top_discounts','Top Discounts'),('perishables','Perishables'),('fruits','Fruits'),('food items','Food Items'),\
        ('spices','Spices'),('vegetables','Vegetables'),('naija ingredients','Naija Ingredients'),('drinks','Drinks'),('oil and sauce','Oil and Sauce'),
        ('baby','Baby and Kids'),('snacks','Snacks'),('toiletries','Toiletries'),('food stuffs','Food Stuffs'),('yam','Yam'),('rice','Rice'),('beans','Beans'),\
            ('garri','Garri'))
        size_categories=(('extra_small','Extra Small'),('small','Small'),('medium','Medium'),('big','Big'),('large','Large'),('extra_large','Extra Large'))
        availability=(('yes','Yes'),('no','No'),('pending','Pending'))
    Categories=Categories()
    product_category=models.CharField(max_length=30,choices=Categories.product_categories)
    weight=models.CharField(verbose_name="Weight (Specify the Units)",null=True,blank=True,max_length=10)
    size=models.CharField(choices=Categories.size_categories,null=True,blank=True,verbose_name='Size of Product',max_length=50)
    price=models.IntegerField(help_text="Enter Price in Naira",default=0)
    original_price=models.IntegerField(null=True,blank=True,verbose_name="Price Without Discount (If Available)",default=0)
    discount=models.IntegerField(null=True,blank=True,help_text="Percentage of Discount (If Available)")
    perishable=models.BooleanField(verbose_name='Is This A Perishable Good(s)?',null=False,default=False)
    product_picture=models.ImageField(upload_to='products',help_text='Upload a Clear Picture of the Product')
    availability=models.CharField(choices=Categories.availability,max_length=10,null=False,default=True,blank=False) 

    def save (self):
        super().save()
        img=Image.open(self.product_picture.path)
        #Resize It
        if 500<img.width<700:
            output_size=(img.height,img.width)
        elif img.width>700:
            output_size=(700,700)
        img.thumbnail(output_size)
        img.save(self.product_picture.path)