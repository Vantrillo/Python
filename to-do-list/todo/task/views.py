from django.shortcuts import render, redirect
from .forms import *
from .models import *
#from django.http import HttpResponse
# Create your views here.
def test(request):
    return render(request, 'task/base.html')
    
def index(request):
    task = Task.objects.all()
    form = TaskForm()
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'task/task_list.html', {'tasks':task, 'forms': form})

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method=='POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'task/edit_task.html', {'forms':form})

def deleteTask(request, pk):
    task=Task.objects.get(id=pk)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request, 'task/delete_task.html',{'task':task})