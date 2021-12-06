from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

class NewTaskForm(forms.Form):
    
    task = forms.CharField(label=" New taks")
    
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    if request.method == "POST":
        request.session["tasks"] = []
        return HttpResponseRedirect(reverse("tasks:index"))
    return render(request,"tasks/index.html",{
        "tasks": request.session["tasks"],
        "form": NewTaskForm()
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request,"tasks/add.html",{
                "form": form
            })
    
    return render(request, "tasks/add.html",{
        "form":NewTaskForm()
    })

