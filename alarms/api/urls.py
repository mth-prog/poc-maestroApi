from django.urls import path 
from .viewset import *

urlpatterns = [ 
	path('teste/', hello_world,
		name = 'tests')

] 
