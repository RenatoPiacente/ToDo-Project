from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.hello_world),
    path('', views.task_list, name='task-list'),
]