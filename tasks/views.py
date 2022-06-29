from django.shortcuts import render
from django.http import HttpResponse

def hello_world(Request):
    return HttpResponse('Hello, World!')


def task_list(Request):
    return render(Request, 'tasks/list.html')


