from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def project1(request):
    return render (request,'fashionapp/project1.html')
