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

def registration_form_view(request):
    if request.method=="POST":
        form=CustomCreationForm(request.POST,request.FILES)
        if form.is_valid():
            updated_form=form.save()
            request.session['id']=updated_form.id
            messages.success(request,"Update Your Information")
            return redirect('profile_registration_update')
    else:
        form=CustomCreationForm
    return render(request,'registration_new.html',{'form':form,'form_title':"User Registration"})

def registration_update_form_view(request):
    if request.session.get('id'):
        initial=get_object_or_404(CustomUser,pk=request.session.get('id'))
    else:
        initial=get_object_or_404(CustomUser,pk=request.user.id)
    if request.method=='POST':
        form=UserUpdateForm(request.POST,request.FILES,instance=initial)
        if form.is_valid():
            updated_form=form.save()
            messages.success(request,'Registration Successful')
            return redirect('homepage')
    else:
        form=UserUpdateForm(instance=initial)
    return render(request,"registration_update.html",{'form':form,'form_title':'User Information Update'})

class Registration_CBV(CreateView):
    model=CustomUser
    form_class=CustomCreationForm
    """fields=('username','password1','password2','email','first_name','last_name','gender','phone_no','state_of_origin','resident_state','home_address','occupation',\
            'profile_pic','region_of_del','location_of_del','transport_ques')"""
    success_url='/producers/registration/update/'
    template_name='registration_new.html'
    form_title=''

    def get_context_data(self,**kwargs):
        context=super(Registration_CBV,self).get_context_data(**kwargs)
        context['form_title']=self.form_title
        return context
    def form_valid(self,form):
        form.save()
        self.request.session['id']=form.instance.id
        messages.success(self.request,"Update Your Information")
        return super(Registration_CBV,self).form_valid(form)

class Registration_Update_CBV(UpdateView):
    model=CustomUser
    form_class=UserUpdateForm
    success_url='/products/'
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
        return super(Registration_Update_CBV,self).form_valid(form)