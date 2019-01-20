from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request): 
	return render(None, 'home.html')

def userhome(request):
	return render(None, 'userhome.html')

def tools(request): 
	return HttpResponse('Tools page coming soon!')

def community(request): 
	return HttpResponse('Community page coming soon!')

def resources(request): 
	return HttpResponse('Resources page coming soon!')

def aboutus(request): 
	return HttpResponse('About Us page coming soon!')
