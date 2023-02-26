from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def tasks(request):
    return render(request,'tasks/task.html')