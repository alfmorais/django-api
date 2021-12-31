from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    
    def get_queryset(self):
        queryset = PontoTuristico.objects.filter(aprovado=True)
        return queryset
    
    """
    def list(self, request, *args, **kwargs):
        dictionary = {
            "nome": "Alfredo de Morais Neto",
            "idade": 29,
            "estado civil": "casado",
        }
        return Response(dictionary)
    """