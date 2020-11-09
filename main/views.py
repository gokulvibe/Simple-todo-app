from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList
from accounts.views import *
# Create your views here.


def home(request):
    todos = TodoList.objects.all()
    
    return render(request,'main/index.html',{'todos':todos})