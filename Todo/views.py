from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


# this view renders some predefined tasks
def index(request):
    tasks = Todo.objects.all()
    context = {'tasks': tasks}
    return render(request, 'todo/index.html', context)


def update(request, id):
    task = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'todo/update.html', {'form': form})


def delete(request, id):
    # Query the to-do table and get all the records
    task = Todo.objects.get(id=id)

    if request.method == 'POST':
        task.delete()
        return redirect('index')

    return render(request, 'todo/delete.html', {'task': task})


def complete(request, id):
    task = Todo.objects.get(id=id)
    setattr(task, 'completed', True)
    task.save()
    return redirect('index')


def add(request):
    form = TodoForm(request.POST or None)

    if form.is_valid():
        form.save()

    return redirect(index)
