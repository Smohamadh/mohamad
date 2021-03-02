from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def list_tasks(request):
    tasks = Task.objects.all()
    count = Task.objects.count()
    return render (request, 'list.html', {'tasks': tasks, 'count':count})

def show_task(request, id):
    return render (request, 'show.html')


def dashboard(request):
    return render (request, 'dashboard.html')


def edit_task(request, id):
    return render (request, 'edit.html')
def delete_task(request, id):
    return render (request, 'delete.html')
def create_task(request):
    return render (request, 'create.html')
def list_persons(request):
    pass
