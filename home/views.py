from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
# Create your views here.


def index(request):
    return render(request, 'home/index.html')

def about(request):
	
	
    return render(request, 'home/about.html')

def blog_item(request):
    return render(request, 'home/blog_item.html')

def blog(request):
    return render(request, 'home/blog.html')

def contactform(request):
	print("hello")
	name_r    = request.POST['yourname']
	email_r   = request.POST['email']
	phone_r = request.POST['phone']
	message_r = request.POST['message']
	c= Client(name=name_r,email=email_r,phone=phone_r,message=message_r)
	c.save()
 
	return render(request,'home/contact.html')

def emailSubscribe(request):
	print("hello")
	email_s = request.POST['email_sub']
	s= Subscribe(email=email_s)
	s.save()

	return render(request, 'home/contact.html')

def contact(request):
	return render(request, 'home/contact.html')

def portfolio(request):
    return render(request, 'home/portfolio.html')

def Home(request):
	return render(request, 'home/index.html')

def service(request):
    return render(request, 'home/service.html')



	