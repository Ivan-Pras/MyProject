from django.shortcuts import render
from  django.http import HttpResponse,HttpRequest
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
    print("LALALALALALA")
    return render(requset, 'classpage.html')

def usernamepage(request, username='undefined'):
    if request.method == "GET":
        print(f'request method GET {request.GET}')
    if request.method == "POST":
        username = request.POST['name1']
    content={
        'username':username,
    }
    return render(request,'username.html',content)