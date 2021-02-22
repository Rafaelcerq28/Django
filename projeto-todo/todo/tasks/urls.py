from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.tasklist),
    path('tasks/<int:id>', views.taskView, name='task-view'),
    path('newtask/',views.newTask,name='new-task'),
    path('edit/<int:id>', views.editTask, name='edit-task'),
    path('delete/<int:id>',views.deleteTask,name='delete-task'),
    path('yourname/<str:name>',views.yourname)
]