from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    
    def get_queryset(self):
        queryset = PontoTuristico.objects.filter(aprovado=True)
        return queryset