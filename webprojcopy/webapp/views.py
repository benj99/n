from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'webapp/homepage.html')

def pictures(request):
    return render(request,'webapp/pictures.html')
