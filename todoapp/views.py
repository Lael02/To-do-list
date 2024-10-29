from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        task_text = request.POST.get('task')
        Task.objects.create(text=task_text)
        return redirect('index')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed  
    task.save()
    return redirect('index')