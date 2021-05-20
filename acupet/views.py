from django.shortcuts import render
from django.http import HttpResponse

# Creat

def index(request):
    return HttpResponse("Hello, world. You're at the ACupet index.")
