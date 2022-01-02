from atracoes.models import Atracao
from rest_framework.viewsets import ModelViewSet

from .serializers import AtracaoSerializer


class AtracoesViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_fields = (
        "id",
        "nome",
        "descricao",
    )
