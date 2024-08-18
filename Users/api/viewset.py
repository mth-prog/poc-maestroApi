from rest_framework import viewsets
from ..models import AuthUser
from .Serializers import ExternalModelSerializer

class ExternalModelViewSet(viewsets.ModelViewSet):
    # Use o banco de dados externo
    queryset = AuthUser.objects.all().filter(is_active=True)
    serializer_class = ExternalModelSerializer
