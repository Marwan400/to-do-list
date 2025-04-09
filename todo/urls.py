from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Dashboard page
    path('todo/', views.todo_list, name='todo_list'),  # My Todo page (list of tasks)
    path('settings/', views.settings, name='settings'),  # Settings page
    path('todo/create/', views.todo_create, name='todo_create'),  # Add new task page
    path('todo/update/<int:pk>/', views.todo_update, name='todo_update'),  # Edit task page
    path('todo/delete/<int:pk>/', views.todo_delete, name='todo_delete'),  # Delete task page
]
