"""
ECommerce URL Configuration
"var popoverTriggerList=[].slice.c  all(document.querySelectorAll('[data-bs-toggle="popover"]'))
    var popoverList=popoverTriggerList.map(function(popoverTriggerEl){return new
    bootstrap.Popover(popoverTriggerEl)})"

"white yam ywllow yam water yam"

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""
from django.contrib import admin
from django.urls import path,include
from . import partner_views,customer_views,views
from django.views.generic import TemplateView
urlpatterns = [path('partnership/registration/',partner_views.Registration_CBV.as_view(form_title="Partnership Registration"),name="partnership_registration"),\
        path('partnership/update/<str:pk>/',partner_views.Registration_Update_CBV.as_view(form_title="Update Information"),name="partnership_update_information"),\
        path('registration/',customer_views.Registration_CBV.as_view(form_title='User Registration'),name="user_registration"),\
        path('registration/update/<str:pk>/',customer_views.Registration_Update_CBV.as_view(form_title="User Update"),name="user_update_information"),\
        path('account/deactivate/<str:pk>/',views.deactivate_activate_view,name="deactivate_account"),\
        path('deactivate/confirm/',TemplateView.as_view(template_name="deactive_confirm.html"),name="deactivate_confirm")]

