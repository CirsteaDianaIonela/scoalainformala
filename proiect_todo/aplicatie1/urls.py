from django.urls import path

from aplicatie1 import views

app_name = 'todo'

urlpatterns = [
    path('', views.TodoView.as_view(), name='lista_todo'),
    path('adaugare/', views.CreateTodoView.as_view(), name='add'),
    path('<int:pk>/update/', views.UpdateTodoView.as_view(), name='modifica'),
    path('<int:pk>/delete/', views.delete_todo, name='sterge'),
    path('<int:pk>/activeaza/', views.activate_task, name='activate'),
    path('deleted_tasks/', views.DeletedTasksView.as_view(), name='deleted_tasks'),
    path('delete_tasks/', views.DeleteTask.as_view(), name='delete_tasks'),
    path('task_done/', views.TaskDoneView.as_view(), name='task_done'),
]
