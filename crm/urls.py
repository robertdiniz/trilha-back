from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import *
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from vendas.views import ProdutoModelViewSet, VendaModelViewSet

router = routers.DefaultRouter()
router.register(r'produtos', ProdutoModelViewSet)
router.register(r'vendas', VendaModelViewSet)

# DRF Spectacular
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vendas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # DRF Spectacular
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
