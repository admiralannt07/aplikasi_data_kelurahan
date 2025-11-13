from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    WargaViewSet,
    PengaduanViewSet,
)

# 1. Bikin routernya
router = DefaultRouter()

# 2. Daftarin ViewSet kita ke router
# Format: router.register(r'prefix_url', NamaViewSet)
router.register(r'warga', WargaViewSet, basename='warga')
router.register(r'pengaduan', PengaduanViewSet, basename='pengaduan')

urlpatterns = [
    path('', include(router.urls)),
]