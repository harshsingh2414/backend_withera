from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun(request):
    return HttpResponse('Hey i am django server')