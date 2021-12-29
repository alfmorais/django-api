from atracoes.models import Atracao
from .serializers import AtracaoSerializer
from rest_framework.viewsets import ModelViewSet


class AtracoesViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
