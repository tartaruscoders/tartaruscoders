from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def loader(request):
    return render(request, 'loader.html')

def home(request):
    return render(request, 'index.html')

def elderaccount(request):
    return render(request, 'sign/elderAccountLogin.html')
