from django.shortcuts import render
from  django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def homepage (request):
    template_name = 'homepage.html'
    return render(request,template_name)

def renderpage(request):
    template_name = 'renderpage.html'
    a = 5+3
    context = {'one':'string one11', 'two':a}
    return render(request, template_name, context)

def classpage(requset):
    return render(requset, 'classpage.html')