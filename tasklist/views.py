from django.shortcuts import redirect, render
from .models import Tasks

def index(request):
    taskList = Tasks.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        done = request.POST.get("done")
        
        if done == "on":
            done = True
        else:
            done = False
        img = request.FILES.get('img')
        task = Tasks(title = title, done = done, img = img)
        task.save()
    return render(request, 'home.html', {'taskList': taskList})


from django.shortcuts import render, redirect
from .models import Tasks

def edit_task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    
    if request.method == 'POST':
        title = request.POST.get("title")
        done = request.POST.get("done")
        img = request.FILES.get('img')

        task.title = title
        task.done = bool(done)
        if img:
            task.img = img
        task.save()
        
        return redirect('/')
    
    context = {
        'task': task
    }
    return render(request, 'edit_task.html', context)
