from core.models import PontoTuristico

# from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        queryset = PontoTuristico.objects.filter(aprovado=True)
        return queryset

    """
    # sobrescrevendo o método GET
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoSerializer, self).list(request, *args, **kwargs)

    # sobrescrevendo o método POST
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoSerializer, self).create(request, *args, **kwargs)

    # sobrescrevendo o método DELETE
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoSerializer, self).destroy(request, *args, **kwargs)

    # sobrescrevendo o método UPDATE
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoSerializer, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoSerializer, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoSerializer, self).partial_update(
            request, *args, **kwargs
        )
    
    @action(method=["GET"], detail=True)
    def nome_da_função(self, request, *args, **kwargs):
        pass
    """
