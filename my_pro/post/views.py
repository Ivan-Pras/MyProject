from django.shortcuts import render
from  django.http import HttpResponse,HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post


# Create your views here.

def homepage (request):
    template_name = 'homepage.html'
    return render(request,template_name)

def renderpage(request):
    template_name = 'renderpage.html'
    a = 5+3
    context = {'one':'string one11', 'two':a}
    return render(request, template_name, context)

def usernamepage(request, username='undefined'):
    if request.method == "GET":
        print(f'request method GET {request.GET}')
    if request.method == "POST":
        username = request.POST['name1']
    content={
        'username':username,
    }
    return render(request,'username.html',content)

def newPost (request):
    if request.GET['name1']:
        newPost=Post()
        data=request.GET
        newPost.text=data['name1']
        newPost.save()
    return redirect('/classpage/')

class ClassPage (ListView):

    model = Post
    template_name = 'classpage.html'
    context_object_name = "all_posts_list"

