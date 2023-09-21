from django.shortcuts import render
from .models import Tasks

def index(request):
    if request.method == "POST":
        title = request.POST.get("title")
        done = request.POST.get("done")
        # Convert 'done' to a Boolean value
        if done == "on":
            done = True
        else:
            done = False
        img = request.FILES.get('img')
        task = Tasks(title = title, done = done, img = img)
        task.save()
    return render(request, 'home.html')