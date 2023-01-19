from django.shortcuts import render, redirect
from .models import list_todo
from .forms import ListForm





def index(request):
    return render(request, "myapp/index.html")

def base(request):
    return render(request, "myapp/base.html")

def basic_table(request):
    return render(request, "myapp/basic_table.html")

def blank(request):
    return render(request, "myapp/blank.html")

def calendar(request):
    return render(request, "myapp/calendar.html")

def buttons(request):
    return render(request, "myapp/buttons.html")

def chartjs(request):
    return render(request, "myapp/chartjs.html")

def form_component(request):
    todos = list_todo.objects.all()
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            return render(request, "myapp/todo_list.html", {'todos':todos})
    else:
        todos = list_todo.objects.all()
        return render(request, "myapp/form_component.html", {'todos':todos})

def gallery(request):
    return render(request, "myapp/gallery.html")

def login(request):
    return render(request, "myapp/login.html")

def lock_screen(request):
    return render(request, "myapp/lock_screen.html")

def morris(request):
    return render(request, "myapp/morris.html")

def panels(request):
    return render(request, "myapp/panels.html")

def responsive_Table(request):
    return render(request, "myapp/responsive_table.html")

def todo_list(request):
    todos = list_todo.objects.all()
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            return render(request, "myapp/todo_list.html", {'todos':todos})
    else:
        todos = list_todo.objects.all()
        return render(request, "myapp/todo_list.html", {'todos':todos})

def general(request):
    return render(request, "myapp/general.html")

def delete(request, list_todo_id):
    todos = list_todo.objects.get(pk=list_todo_id)
    todos.delete()
    return redirect("todo_list")

def update(request, list_todo_id):
    if request.method == 'POST':
        todos = list_todo.objects.get(pk=list_todo_id)
        form = ListForm(request.POST or None, instance=todos)
        if form.is_valid:
            form.save()
            return redirect("todo_list")
    else:
        todos = list_todo.objects.all()
        return render(request, 'myapp/update.html', {'todos': todos})


def yesfinished(request, list_todo_id):
    todos = list_todo.objects.get(pk=list_todo_id)
    todos.finished = True
    todos.save()
    return redirect("todo_list")

def nofinished(request, list_todo_id):
    todos = list_todo.objects.get(pk=list_todo_id)
    todos.finished = False
    todos.save()
    return redirect("todo_list")