from django.shortcuts import render,redirect,get_object_or_404
from order.models import Order
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class Profile_Page(LoginRequiredMixin,ListView):
    login_url="/accounts/login/"
    model=Order
    template_name='profile_page.html'
    context_object_name='orders'
    def get_queryset(self):
        order_model=Order.objects.filter(buyer__pk=self.request.user.id).order_by('-date')
        return order_model