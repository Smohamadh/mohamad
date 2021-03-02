
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks', views.list_tasks, name = 'list_tasks'),
    path('show_task/<int:id>', views.show_task, name = 'show_task'),
    path('tasks/<int:id>/edit', views.edit_task, name = 'edit_task'),
    path('tasks/<int:id>/delete', views.delete_task, name = 'delete_task'),
    path('tasks/create>', views.create_task, name = 'create_task'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('persons', views.list_persons, name = 'list_persons'),
]
