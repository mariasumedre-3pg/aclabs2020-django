from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def hello(request):
    "hello view"
    return HttpResponse(content="Hello!")
