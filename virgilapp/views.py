from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request): 
	return render(None, 'home.html')

def userhome(request):
	return render(None, 'userhome.html')

def tools(request): 
	return HttpResponse('tools page comin soon promise')

def community(request): 
	return HttpResponse('community page comin soon trust')

def resources(request): 
	return HttpResponse('resources page comin soon bless up')

def aboutus(request): 
	return HttpResponse('about us page comin soon bless down')
