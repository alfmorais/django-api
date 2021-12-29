from rest_framework.viewsets import ModelViewSet
from .serializers import AvaliacaoSerializer
from avaliacoes.models import Avaliacoes

class AvaliacoesViewSet(ModelViewSet):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer