from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('edit-task/<int:task_id>/', views.edit_task, name="edit-task"),
    path('delete-task/<int:task_id>/', views.delete_task, name="delete-task"),
]
