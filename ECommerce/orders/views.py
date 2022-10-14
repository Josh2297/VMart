from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.

def AjaxCall(request):
    data_post=json.load(request)['data']
    print(data_post)
    return JsonResponse({'data':'This is Good'},status=200)
