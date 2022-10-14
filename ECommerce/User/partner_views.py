from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
# from django.contrib.auth import login,authenticate
from .models import CustomUser
from .partner_form import CustomCreationForm,UserUpdateForm
# from django.contrib.auth.decorators import permission_required,login_required,user_passes_test
from django.contrib.auth.models import Group
from PIL import Image
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .random_id import random_generator
from datetime import datetime


# Create your views here.

'''def registration_form_view(request):
    if request.method=="POST":
        form=CustomCreationForm(request.POST,request.FILES)
        if form.is_valid():
            updated_form=form.save(commit=False)
            updated_form.partnership_status='pending'
            updated_form.save()
            customer_group=Group.objects.get(name='partners')
            updated_form.groups.add(customer_group)
            form.save_m2m()
            messages.success(request,'Registration Successful')
            return redirect('/accounts/login/')
    else:
        form=CustomCreationForm
    return render(request,'registration_new.html',{'form':form,'form_title':"Partnership Registration"})

def partnership_update_form_view(request):
    if request.session.get('id'):
        initial=get_object_or_404(CustomUser,pk=request.session.get('id'))
    else:
        initial=get_object_or_404(CustomUser,pk=request.user.id)
    if request.method=='POST':
        form=UserUpdateForm(request.POST,request.FILES,instance=initial)
        if form.is_valid():
            updated_form=form.save(commit=False)
            customer_group=Group.objects.get(name='partners')
            updated_form.groups.add(customer_group)
            updated_form.partnership_status='pending'
            updated_form.save()
            messages.success(request,'Registration Successful')
            return redirect('/accounts/login/')
    else:
        form=UserUpdateForm(instance=initial)
    return render(request,"registration_update.html",{'form':form,'form_title':'Partnership Information Update'})'''

class Registration_CBV(CreateView):
    model=CustomUser
    form_class=CustomCreationForm
    success_url='/accounts/login/'
    template_name='registration_new.html'
    form_title=''


    def get_context_data(self,**kwargs):
        context=super(Registration_CBV,self).get_context_data(**kwargs)
        context['form_title']=self.form_title
        return context

    def form_valid(self,form):
        updated_form=form.save(commit=False)
        updated_form.id=random_generator(form.cleaned_data.get('first_name'),form.cleaned_data.get('email'))
        updated_form.date_joined=datetime.now()
        updated_form.partnership_status='pending'
        updated_form.save()
        customer_group=Group.objects.get(name='partners')
        updated_form.groups.add(customer_group)
        form.save_m2m()
        messages.success(self.request,'Registration Successful')
        return super(Registration_CBV,self).form_valid(form)

class Registration_Update_CBV(LoginRequiredMixin,UpdateView):
    model=CustomUser
    form_class=UserUpdateForm
    success_url='/profile/'
    template_name='registration_update.html'
    form_title=''
    login_url="/accounts/login/"

    def get_context_data(self,**kwargs):
        context=super(Registration_Update_CBV,self).get_context_data(**kwargs)
        context['form_title']=self.form_title
        return context
    def form_valid(self,form):
        form.save()
        messages.success(self.request,"Information Update: Successful")
        return super(Registration_Update_CBV,self).form_valid(form)