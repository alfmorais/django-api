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
    # sobrescrevendo o método GET
    def list(self, request, *args, **kwargs):
        dictionary = {
            "nome": "Alfredo de Morais Neto",
            "idade": 29,
            "estado civil": "casado",
        }
        return Response(dictionary)
    
    # sobrescrevendo o método POST
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    # sobrescrevendo o método DELETE
    def destroy(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    # sobrescrevendo o método UPDATE
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @action(method=["GET"], detail=True)
    def nome_da_função(self, request, pk=None):
        return super().update(request, *args, **kwargs)
    
    """