from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoItemForm

# List all To-Do items
def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

# Create a new To-Do item
def todo_create(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TodoItemForm()
    return render(request, 'todo/todo_form.html', {'form': form})

# Update a To-Do item
def todo_update(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TodoItemForm(instance=todo)
    return render(request, 'todo/todo_form.html', {'form': form})

# Delete a To-Do item
def todo_delete(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('dashboard')
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})

# Dashboard View
def dashboard(request):
    # Fetching all tasks from the database
    todos = TodoItem.objects.all()  # Ensure you're querying the correct table
    return render(request, 'todo/dashboard.html', {'todos': todos})

# My Todo View (Already exists)
def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

# Settings View
def settings(request):
    return render(request, 'todo/settings.html')  # Create a settings template