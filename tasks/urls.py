from django import path

from . import views

urlpatterns = [
    path('helloworld/', views.hello_world),
]