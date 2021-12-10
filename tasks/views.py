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
            return render(request,"tasks/add.html",{
                "form": form
            })
    
    return render(request, "tasks/add.html",{
        "form":NewTaskForm()
    })

def insert_task(task):
    # creamos un objeto Task y usamos el metodo save para almacenar
    # en la BD
    t = Task(task = task)
    t.save()