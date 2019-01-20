from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
	path('', views.home, name = 'genhome'),
	path('me/', views.userhome, name = 'userhome'),
	path('tools/', views.tools, name = 'tools'),
	path('community/', views.community, name = 'community'),
	path('resources/', views.resources, name = 'resources'),
	path('aboutus/', views.aboutus, name = 'aboutus'),
	]
