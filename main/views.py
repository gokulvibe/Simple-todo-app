from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList
from accounts.views import *
# Create your views here.


def home(request):
    
    if request.user.is_authenticated:
            username = request.user.id
            todos = TodoList.objects.filter(owner=username)
            return render(request,'main/index.html',{'todos':todos})
    else:
        return render(request,'main/index.html')
    