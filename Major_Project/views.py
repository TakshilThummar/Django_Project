from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.

def index(request):
    return render(request, 'Major_Project/index.html', {})
    
def about(request):
    return render(request, 'Major_Project/about.html', {})

def service(request):
    return render(request, 'Major_Project/service.html', {})

def project(request):
    return render(request, 'Major_Project/project.html', {})

def contact(request):
    return render(request, 'Major_Project/contact.html', {})

def insertuser(request):
    vuname = request.POST['name']
    vuemail = request.POST['email']
    vunumber = request.POST['number']
    vusubject = request.POST['subject']
    vucontent = request.POST['content']

    cn = Contact(name = vuname, email = vuemail, number = vunumber, subject = vusubject, content = vucontent)
    
    cn.save()
    
    return render(request, 'Major_Project/index.html', {})
