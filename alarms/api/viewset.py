from .functions import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def ec2(request, format=None):
    if request.method == 'GET':
        return Response(list_automation(name=request.data['Name']))
   
    if request.method == 'POST':
         # create alarme
        return Response(execution_automation(name=request.data['Name']))
