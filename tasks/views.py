from django.shortcuts import render
from django import HttpResponse

def hello_world(Request):
    return HttpResponse('Hello, World!')
