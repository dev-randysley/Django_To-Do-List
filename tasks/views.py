from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Task
# Create your views here.

class NewTaskForm(forms.Form):
    
    task = forms.CharField(label="",widget= forms.TextInput
                           (attrs={'placeholder':'New Task'})
                           )


def index(request):
    return render(request,"tasks/index.html",{
        "tasks": Task.objects.all(),
        "form": NewTaskForm()
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            new_task = form.cleaned_data["task"]
            insert_task(new_task)
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request,"tasks/index.html",{
                "form": form
            })
    
    return render(request, "tasks/add.html",{
        "form":NewTaskForm()
    })


def edit(request, task_id):
    task = Task.objects.get(pk = task_id)
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            if "save" in request.POST:
                task = form.cleaned_data["task"]
                update_task(task,task_id)
                HttpResponseRedirect(reverse("tasks:index"))
            else:
                return render(request, "tasks/index.html",{
                    "tasks": Task.objects.all(),
                    "form": NewTaskForm()
                })
    return render(request, "tasks/edit.html",{
        "task": task,
        "form":NewTaskForm()
    })


def update_task(task,task_id):
    current = Task.objects.get(pk = task_id)
    current.task = task
    current.save()

def insert_task(task):
    # creamos un objeto Task y usamos el metodo save para almacenar
    # en la BD
    t = Task(task = task)
    t.save()

