from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def view_tasks(request):
    return render(request,'tasks/task.html')

def add_task(request):
    
    return render(request,'tasks/task.html')

def edit_task(request):
    return render(request,'tasks/task.html')

def delete_task(request):
    return render(request,'tasks/task.html')