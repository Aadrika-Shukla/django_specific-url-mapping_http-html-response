from django.shortcuts import render
from django.http import HttpResponse

def app1str(request):
    return HttpResponse('this is string as http response for app1')

# Create your views here.
