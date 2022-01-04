"""turismo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from atracoes.api.viewsets import AtracoesViewSet
from avaliacoes.api.viewsets import AvaliacoesViewSet
from comentarios.api.viewsets import ComentariosViewSet
from core.api.viewsets import PontoTuristicoViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from enderecos.api.viewsets import EnderecosViewSet
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r"pontoturistico", PontoTuristicoViewSet, basename="PontoTuristico")
router.register(r"atracoes", AtracoesViewSet)
router.register(r"comentarios", ComentariosViewSet)
router.register(r"avaliacoes", AvaliacoesViewSet)
router.register(r"enderecos", EnderecosViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api-token-auth/", obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
