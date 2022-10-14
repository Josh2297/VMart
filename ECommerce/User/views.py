from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import CustomUser
from .partner_form import CustomCreationForm,UserUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required,login_required,user_passes_test
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from datetime import datetime
from PIL import Image
from django.views import View
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView


# Create your views here.

#Deactivate account
@login_required(login_url="/accounts/login/")
def deactivate_activate_view(request,pk):
    user_id=pk;user=get_object_or_404(CustomUser,pk=user_id)
    if user.id==request.user.id and user.is_active: # Deactivate Account
        user.is_active=False
        user.save();messages.info(request,'Account Deactivated Successful')
        return redirect('/products/')
    else: # Reactivate
        user.is_active=True
        user.save();messages.success(request,'Account Reactivated')
        return redirect('/accounts/login/')

# Delete View

class DeleteUserView(DeleteView):
    model=CustomUser
    success_url="/products/"

'''class UserList(ListView):
    model=CustomUser
    template_name='users_list.html'
    context_object_name="user_list"

class Registration_Update_CBV(UpdateView):
    model=CustomUser
    form_class=UserUpdateForm
    success_url='/profile/'
    template_name='registration_update.html'
    form_title=''

    def get_context_data(self,**kwargs):
        context=super(Registration_Update_CBV,self).get_context_data(**kwargs)
        context['form_title']=self.form_title
        return context
    def form_valid(self,form):
        form.save()
        self.request.session['id']=form.instance.id
        messages.success(self.request,"Information Update: SuccessFul")
        return super(Registration_Update_CBV,self).form_valid(form)'''