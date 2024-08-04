from rest_framework.decorators import api_view
from rest_framework.response import Response
from .functions import *

@api_view(['GET', 'POST'])
def ec2(request):
    if request.method == 'GET':
        return Response(list_automation(name='NewRunbook'))
    if request.method == 'POST':
         # create alarme
        return Response(execution_automation(name=request.data['Name']))
