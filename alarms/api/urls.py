from django.urls import path 
from .viewset import *

urlpatterns = [ 
	path('ec2/', ec2,
		name = 'ec2_alarm_create')

] 
